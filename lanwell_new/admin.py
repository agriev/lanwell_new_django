from django.contrib import admin

from lanwell_new.models import CompletedProject,ProjectTag,CustomerRequest
# Register your models here.

admin.site.register(CompletedProject)
admin.site.register(ProjectTag)
admin.site.register(CustomerRequest)
