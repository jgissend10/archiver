def dashboard_view(view):
    def inner(request, *args, **kwargs):
        context = {'request': request, 'user': request.user}
        kwargs['context'] = context
        return view(request, *args, **kwargs)
    return inner
