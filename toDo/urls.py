from django.urls import path,include
from .api import ToDoViewSet
from rest_framework.routers import DefaultRouter
from .views import todo_list

router = DefaultRouter()
router.register('todo',ToDoViewSet)

urlpatterns = [
    path('',todo_list),
    path('api/', include(router.urls)),
]
