"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from webapp.views.project_views import ProjectView, ProjectCreateView, IndexView, ProjectUpdateView, ProjectDeleteView
from webapp.views.task_views import ProjectTaskCreateView, TaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/tasks/add/', ProjectTaskCreateView.as_view(), name='project_task_create'),
    # path('tasks/add/', TaskCreateView.as_view(), name='task_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/', include('accounts.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

