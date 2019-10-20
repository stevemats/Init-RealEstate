from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    # get the last 3 published listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    # context for rendering    
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # get all realtors
    realtors = Realtor.objects.all()
    
    # get only realtors that are mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    
    # context for rendering
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
