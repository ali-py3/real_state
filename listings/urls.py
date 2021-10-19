from django.urls import path

from . import views
# app_name = "lister"
from .views import SearchResultsView
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    # path('<slug:slug>', views.category, name='category'),
    # path('<slug:slug>/page/<int:page>', views.category, name='category'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
