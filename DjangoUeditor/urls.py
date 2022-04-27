# coding:utf-8
from django import VERSION
from .widgets import UEditorWidget, AdminUEditorWidget
from .views import get_ueditor_controller
from django.urls import include, re_path


urlpatterns = [
    re_path(r'^controller/$', get_ueditor_controller),
]
