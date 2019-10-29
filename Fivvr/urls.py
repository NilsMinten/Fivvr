"""Fivvr URL Configuration

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
from django.urls import path
from Services import views as serviceviews
from CustomUsers import views as userviews

urlpatterns = [
    # --- Admin panel url ---#
    path('', admin.site.urls),

    # --- User api urls  --- #
    # User URLs
    path('user/create', userviews.create_user, name='create_user'),
    path('user/login', userviews.login_user, name='create_user'),
    path('user/object_karma/<int:user_id>', userviews.object_karma, name='create_user'),
    # Service URLs
    path('service', serviceviews.load_services, name='display_services'),
    path('service/<int:service_id>', serviceviews.load_service, name='load_service'),
    path('service/create', serviceviews.create_service, name='create_service'),
    path('service/delete/<int:service_id>', serviceviews.delete_service, name='delete_services'),
    path('service/edit/<int:service_id>', serviceviews.edit_service, name='edit_services'),
    path('service/upvote/<int:service_id>', serviceviews.upvote_service, name='upvote_service'),
    path('service/buy/<int:service_id>', serviceviews.buy_service, name='buy_service'),
    path('service/cancel/<int:service_id>', serviceviews.cancel_service, name='cancel_service'),

    # --- Admin urls  --- #
    # Karma management
    path('administrator/karma/<int:user_id>', userviews.admin_view_karma_objections, name='view_karma_objections'),
    path('administrator/karma/<int:objection_id>/accept',
         userviews.admin_approve_karma_objection, name='accept_karma_objection'),
    path('administrator/karma/<int:objection_id>/deny',
         userviews.admin_deny_karma_objection, name='deny_karma_objection'),
]
