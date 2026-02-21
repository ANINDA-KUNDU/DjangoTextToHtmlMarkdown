from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('code', views.code, name = "code"),
    path('mark-down/<int:pk>', views.mark_down, name = "mark_down"),
    path('create-markdown', views.create_markdown, name = "create_markdown"),
]