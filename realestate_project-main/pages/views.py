from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import ward_choices, price_choices, subcounty_choices

def index(request):
    """ Render index page """
    # [:number] limits entries to specified number
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'wards_choices': ward_choices,
        'price_choices': price_choices,
        'subcounty_choices': subcounty_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    """ render about page """
    realtors = Realtor.objects.order_by('-hire_date')

    # get sellser of the months
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

