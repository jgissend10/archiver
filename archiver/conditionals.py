from archiver.models import ArchiverApp

def user_can_manage(context, *args, **kwargs):
    app_label = kwargs.pop('app_label', args[0] if len(args) else None)
    return ArchiverApp.objects.filter(creators=context['user'].id, app_label=app_label)

def user_can_see(context, *args, **kwargs):
    app_label = kwargs.pop('app_label', args[0] if len(args) else None)
    app = ArchiverApp.objects.get(app_label=app_label)
    return app.public or ArchiverApp.objects.filter(creators=context['user'].id, app_label=app_label)
