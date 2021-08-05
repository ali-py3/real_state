from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('category/<slug:slug>/page/<int:page>', views.category, name='category'),

]
