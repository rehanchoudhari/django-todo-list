from django.contrib import admin
from .models import DailyTask

class DailyTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'complete')


admin.site.register(DailyTask, DailyTaskAdmin)
