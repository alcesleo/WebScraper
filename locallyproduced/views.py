from django.shortcuts import render, redirect
from locallyproduced.models import Producer
from locallyproduced.scraper import Scraper

# create your views here.
def show(request):
    """Show the contents of the db"""
    return render(request,
           'locallyproduced/producers.html',
           {'producers': Producer.objects.all()})

def scrape(request):
    """Scrape the site, then redirect to show db"""
    s = Scraper()
    s.scrape()
    return redirect('locallyproduced.views.show')
