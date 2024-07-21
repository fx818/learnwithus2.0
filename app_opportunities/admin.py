from django.contrib import admin

# Register your models here.

from .models import jobModel, InternshipModel, scholarshipModel, CompetetionModel

class InternshipModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'desc')
    list_filter = ('title',)
    search_fields = ('title', 'link')

admin.site.register(InternshipModel, InternshipModelAdmin)

class CompetetionModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'desc')
    list_filter = ('title',)
    search_fields = ('title', 'link')

admin.site.register(CompetetionModel, CompetetionModelAdmin)

class scholarshipModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'desc')
    list_filter = ('title',)
    search_fields = ('title', 'link')

admin.site.register(scholarshipModel, scholarshipModelAdmin)

class jobModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'desc')
    list_filter = ('title',)
    search_fields = ('title', 'link')

admin.site.register(jobModel, jobModelAdmin)
