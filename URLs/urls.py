from django.urls import path

from . import views

urlpatterns = [path('new_url', views.new_url, name='new_url'),
                path('<str:sh_url>', views.handle_short, name='short'),]