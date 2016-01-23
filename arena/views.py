from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import Document
from .forms import DocumentForm
# Create your views here.
@csrf_exempt
def success(request):
    return render(request,'success.html')

@csrf_exempt
def slf(request):
    return render(request,'slf.html')

@csrf_exempt
def redirect(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            return render_to_response('success.html',context_instance=RequestContext(request))

        else:
            return render_to_response('fnv.html',context_instance=RequestContext(request))

    else:
        form = DocumentForm()
    return render_to_response('failure.html',context_instance=RequestContext(request))
