from django.contrib import admin
from .models import StopMotion

# Register your models here.
class StopMotionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'video',
        'description',
    )


admin.site.register(StopMotion, StopMotionAdmin)
