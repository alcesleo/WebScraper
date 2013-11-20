from django.shortcuts import render
from locallyproduced.models import Producer
from locallyproduced.scraper import Scraper

# create your views here.
def show(request):

    # update the results
    s = Scraper()
    s.scrape()

    # render the contents of db
    return render(request,
           'locallyproduced/producers.html',
           {'producers': Producer.objects.all()})
