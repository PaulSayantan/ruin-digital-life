from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(CustomUser)
# admin.site.register(Image)
# admin.site.register(Thought)

class ThoughtResource(resources.ModelResource):
    class Meta:
        model=Thought

class ImageResource(resources.ModelResource):
    class Meta:
        model=Image

class ThoughtAdmin(ImportExportModelAdmin):
    resource_class = ThoughtResource

class ImageAdmin(ImportExportModelAdmin):
    resource_class=ImageResource

admin.site.register(Thought, ThoughtAdmin)
admin.site.register(Image,ImageAdmin)