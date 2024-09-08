from django.urls import path

from . import views

urlpatterns = [
    path('', views.shorten_form),
    path('new/', views.shorten_link, name='shorten_link'),
    path('<str:short_hash>/', views.redirect_view),
]
