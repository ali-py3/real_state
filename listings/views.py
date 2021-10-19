from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing, Category
from django.views.generic import TemplateView, ListView
from django.db.models import Q

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    mapbox_access_token = 'pk.eyJ1IjoicHpra2siLCJhIjoiY2tyeHA4czZ5MDl6MzJ2bXNybjNjd21mYSJ9.ZMQr197_oeR2QvOGvN8YCA'
    context = {
        'listings': paged_listings,
        'mapbox_access_token': mapbox_access_token,
    }

    return render(request, 'listings/listings.html', context)


# def category(request, slug):
#     # article_list = category.article.published()
#
#     context = {
#         "category": get_object_or_404(Category, slug=slug, status=True)
#     }
#     return render(request, 'listings/category.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


class SearchResultsView(ListView):
    model = Listing
    template_name = 'listings/search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Listing.objects.filter(
            Q(title__icontains=query) | Q(address__icontains=query) | Q(description__icontains=query)
        )

        return object_list