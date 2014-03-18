from django.shortcuts import render_to_response

from archiver.models import ArchiverApp
from archiver.decorators import dashboard_view

def cover(request):
	context = {}
	return render_to_response('archiver/cover.html', context)

@dashboard_view
def dashboard(request, context):
    context['creators'] = ArchiverApp.objects.get(app_label='archiver').creators.all()
    return render_to_response('archiver/dashboard.html', context)
