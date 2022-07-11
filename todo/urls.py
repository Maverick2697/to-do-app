from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='mytasks'),
    path('task_details/<int:pk>/', TaskDetails.as_view(), name= 'task_details'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),

    
]
