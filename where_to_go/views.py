from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place

def serialize_place(place):
    return {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": None
          }
        }

def show_index_page(request):
    places_geojson = {'type': 'FeatureCollection'}
    places = Place.objects.all()
    places_content = [serialize_place(place) for place in places]
    places_geojson['features'] = places_content
    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=context)