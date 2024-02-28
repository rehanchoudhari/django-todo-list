from rest_framework import routers
from .views import DailyTaskView

app_name = 'task_app'

router = routers.DefaultRouter()
router.register('todo', DailyTaskView)