from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    ## Displaying the latest 3 listings on the home page
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings' : listings,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get All Realtors
    realtor = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtor,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, 'pages/about.html', context)
