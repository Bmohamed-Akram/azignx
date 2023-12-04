from django.contrib import admin
from Home.models import service,contact,projects,subscribe

# Register your models here.

admin.site.register(service)
admin.site.register(projects)
admin.site.register(contact)
admin.site.register(subscribe)