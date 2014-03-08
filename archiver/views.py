from django.shortcuts import render_to_response

def dashboard(request):
    context = {}
    return render_to_response('archiver/dashboard.html', context)
