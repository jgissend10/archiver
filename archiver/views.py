from django.shortcuts import render_to_response

from archiver.models import ArchiverApp

def cover(request):
	context = {}
	return render_to_response('archiver/cover.html', context)

def dashboard(request):
    context = {}
    if request.user.is_authenticated():
        context['enabled_apis'] =  ArchiverApp.objects.filter(creators=request.user)
        context['models'] = [app.get_models() for app in context['enabled_apis']]
        context['permissions'] = [app.get_permissions() for app in context['enabled_apis']]
        context['request'] = request
        return render_to_response('archiver/dashboard.html', context)
