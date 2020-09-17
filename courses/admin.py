from django.contrib import admin
from .models import Subject, Course, Module

#rename the admin header
admin.site.site_header = 'JERRY E-LEARNING'

# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

# making the table an inline model
class ModuleInline(admin.StackedInline):
    model = Module
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    # combining the module with the course model
    #inlines = [ModuleInline]
