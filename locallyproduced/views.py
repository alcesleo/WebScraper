from django.shortcuts import render
from locallyproduced.models import Producer

# Create your views here.
def show(request):
    return render(request,
           'locallyproduced/producers.html',
           {'producers': Producer.objects.all()})
