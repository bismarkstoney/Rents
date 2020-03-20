from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import  price_choices, bedroom_choices, state_choices
def index(request):
    listings=Listing.objects.order_by('-list_datae').filter(is_published=True)[:3]
    context={
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors=Realtor.objects.all()
    is_mvp=Realtor.objects.filter(is_mvp=True)
    context={
        'realtors': realtors,
        'is_mvp': is_mvp
    }
    return render(request, 'pages/about.html', context)