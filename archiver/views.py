from django.shortcuts import render
from django.template import RequestContext

from archiver.models import ArchiverApp
from archiver.decorators import dashboard_view

def cover(request):
	context = {}
	return render(request, 'archiver/cover.html', context)

@dashboard_view('archiver')
def dashboard(request, context):
    return render(request, 'archiver/dashboard.html', context)
