from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import subcounty_choices, ward_choices, price_choices

def index(request):
    """ View to render template displaying all listings """
    # listings = Listing.objects.all() for all listings
    # listings should be ordered based on date added, and only display listings if is_published is True
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #6 listings per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """ View to render template displaying individual home listing """
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    """ View to render Search template """
    queryset_list = Listing.objects.order_by('-list_date')

    # search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = (
            queryset_list.filter(description__icontains=keywords) | 
            queryset_list.filter(subcounty__iexact=keywords) | 
            queryset_list.filter(eircode__iexact=keywords) |
            queryset_list.filter(suburb__iexact=keywords)
            )
    
    # search by eircode
    if 'code' in request.GET:
        code = request.GET['code']
        if code:
            queryset_list = queryset_list.filter(code__iexact=code)
    
    # search by county
    if 'subcounty' in request.GET:
        subcounty = request.GET['subcounty']
        if subcounty:
            queryset_list = queryset_list.filter(subcounty__iexact=subcounty)
    
    # search by number of bedrooms
    if 'ward' in request.GET:
        ward = request.GET['ward']
        if ward:
            queryset_list = queryset_list.filter(ward__lte=ward)
    
    # search by price (up to selected range)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    # search by lease type (buy or rent)
    if 'lease_type' in request.GET:
        lease_type = request.GET['lease_type']
        if lease_type:
            queryset_list = queryset_list.filter(lease_type__iexact=lease_type)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'bedroom_choices': ward_choices,
        'price_choices': price_choices,
        'county_choices': subcounty_choices,
        'listings': paged_listings,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
