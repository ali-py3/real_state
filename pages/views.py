from realtors.models import Realtor
from listings.models import Listing, Category
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator


from listings.choices import price_choices, bedroom_choices, state_choices



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'category': Category.objects.filter(status=True)
    }

    return render(request, 'pages/index.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug, status=True)
    # article_list = category.cater.published()
    # paginator = Paginator(article_list, 3)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)
    context = {
        "category": category,
        # 'articles':paged_listings
    }
    return render(request, 'listings/category.html', context)





def about(request):

    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
