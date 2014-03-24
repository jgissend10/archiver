from archiver.models import ArchiverApp

app_info = {
    'name' : 'ACM Archiver',
    'app_label' : 'acm_archiver', 
    'flavor_text' : "Data for all!",
    'description' : "ACM Archiver is a project dedicated to making data easier to store and retrive for the students of the CECS department at the J. B. Speed School of Engineering.",
    'public' : True,
    'github' : "jgissend10/archiver"
} 

try:
    app = ArchiverApp.objects.get(app_label=app_info['app_label'])
    for key, value in app_info.iteritems():
        setattr(app, key, value)
    app.save()
except ArchiverApp.DoesNotExist:
    app = ArchiverApp(**app_info)
    app.save()

