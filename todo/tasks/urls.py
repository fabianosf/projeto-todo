from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'), # list.html
    path('task/<int:id>', views.taskView, name='task-view'), # task.html
    path('newtask/', views.newTask, name='new-task'), # addtask.html
    path('edit/<int:id>', views.editTask, name='edit-task'), # editask.html
    path('changestatus/<int:id>', views.changeStatus, name='change-status'), # changestatus.html
    path('delete/<int:id>', views.deleteTask, name='delete-task'), # deletetask.html
    path('yourname/<str:name>', views.yourName, name='yourname'),
]
