from django.urls import path

from . import views
# app_name = "lister"
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('<slug:slug>', views.category, name='category'),
    # path('<slug:slug>/page/<int:page>', views.category, name='category'),
    path('search', views.search, name='search'),
]
