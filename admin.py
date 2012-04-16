from django.contrib import admin
from obieconnect.models import Department, Professor, Course

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("shortname",)}
    
#class ProfessorAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("firstname" + "-" + "lastname",)}

#class CourseAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("department" + "level",)}
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
 
     
