from django.contrib import admin

from .models import CourseModel, ApplicationModel


@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ApplicationModel)
class CourseAdmin(admin.ModelAdmin):
        list_display = ('cousre','preferred_start_date','payment_method', 'status',)