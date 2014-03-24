from django.contrib.auth.forms import AuthenticationForm as auth_form
from django.core.context_processors import csrf
from archiver.models import ArchiverApp

def dashboard_view(applabel):
    def view_decorator(view):
        def inner(request, *args, **kwargs):
            context = {'request': request, 'user': request.user}
            if not request.user.is_active:
                context['form'] = auth_form(request)
                context['next'] = '/dashboard'
                context.update(csrf(request))
            context['app'] = ArchiverApp.objects.get(app_label=applabel)
            kwargs['context'] = context
            return view(request, *args, **kwargs)
        return inner
    return view_decorator
