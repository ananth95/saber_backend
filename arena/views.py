from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Document
from .forms import DocumentForm

import os, sys, json
# Create your views here.

class myLog:
    def __init__(self, fn, tn, bid, gid):
        self.fname   = fn
        self.tname   = tn
        self.bot_uri = "/media/bots/%s/%s" % (tn, fn)
        self.error   = "/media/logs/%s/bot%d.error.log" % (gid, bid)
        self.input   = "/media/logs/%s/bot%d.input.log" % (gid, bid)
        self.output  = "/media/logs/%s/bot%d.output.log"  % (gid, bid)
        self.replay  = "/media/logs/%s/game_replay.js"  % (gid)

@csrf_exempt
def success(request):
    return render(request,'success.html')

@csrf_exempt
def redirect(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            game_id = '5655'
            bot_fnames = ["bot6.py", "bot7.py"]
            game_worked = False
            ret = os.system("bash ./launch_saber.sh")
            if ret == 0:
                game_worked = True
            logs = []
            log_links_json = []
            for bid, bfile in enumerate(bot_fnames):
                info = {'fname'   : bfile,
                        'tname'   : "team%d" % bid,
                        'bot_uri' : "/media/bots/%s/%s" % ("team%d"%bid, bfile),
                        'error'   : "/media/logs/%s/bot%d.error.log" % (game_id, bid),
                        'input'   : "/media/logs/%s/bot%d.input.log" % (game_id, bid),
                        'output'  : "/media/logs/%s/bot%d.output.log"  % (game_id, bid),
                        'replay'  : "/media/logs/%s/game_replay.js" % (game_id)}
                logs.append(myLog(bfile, info['tname'], bid, game_id))
                log_links_json.append(info)
            
            t = loader.get_template("success.html")
            c = {
                    'status'       : game_worked,
                    'bot_count'    : 2,
                    'bot_fnames'   : bot_fnames,
                    'tnames'       : ["team0, team1"],
                    'log_links'    : logs,
                    'game_log'     : "/media/logs/%s/game_log.r0.log" % game_id,
                    'json_replay'  : "/media/logs/%s/game_replay.js" % game_id,
                    'log_json'     : json.dumps(log_links_json, sort_keys=True)
                }
            return HttpResponse(t.render(c, request))
        else:
            return render(request, 'fnv.html')
    return render(request, 'failure.html')
