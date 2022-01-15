from django.shortcuts import render
from launcher.models import Housing
from django.conf import settings

# Create your views here.


def index(request):
    # TODO: load csv data into our housing model -- is this for a particular day??
    # TODO: get best housing options 
    housing = Housing.objects.all() # get complete list of housing
    # TODO: additional filtering of housing objects in db based on user requests (i.e. they want something < 2 km and has showers)
    # TODO: link to Google Maps API so we have a visual of these places
    context = {
        'housing': housing,
        'google_api_key': settings.GOOGLE_API_KEY
    }

    # send request to the index page with the housing data passed in
    return render(request, 'index.html', context)