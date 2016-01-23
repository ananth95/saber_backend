from django.shortcuts import render
from .models import Document
from .forms import DocumentForm

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'list.html')

@csrf_exempt
def success(request):
    return render(request,'success.html')

@csrf_exempt
def slf(request):
    return render(request,'slf.html')

@csrf_exempt
def list(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            return render_to_response(
            'success.html',
            context_instance=RequestContext(request))

        else:
            return render_to_response(
            'slf.html',
            context_instance=RequestContext(request))

    else:
        form = DocumentForm()

    return render_to_response(
        'failure.html',
        context_instance=RequestContext(request))
