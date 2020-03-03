#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('help/', views.help),
    path('login/', views.login),
    path('logout/', views.logout),
    path('settings/', views.block_settings),
    path('message/', views.message),

    path('music/', views.music),
    path('music_md/', views.modify_article),

    path('article/', views.article),
    path('article_md/', views.modify_article),

    path('edit_message/', views.EditMessageView.as_view()),
    path('message_audit/', views.AuditMessage.as_view()),
    path('role/', views.role),
    path('edit_role/', views.EditRoleView.as_view()),
    path('list_sysuser/', views.list_sys_user),
    path('edit_sysuser/', views.EditSysUserView.as_view()),

]
