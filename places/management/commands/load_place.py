import os
#import json
import requests
from places.models import Place, PlaceImage
from django.core.management.base import BaseCommand, CommandError
from django.core import files
from PIL import Image
from io import BytesIO

class Command(BaseCommand):
    help = 'Add new places'
    
    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        url = options['url']
        
        """
        with open(url, encoding='utf-8') as json_file:
            place_json = json.load(json_file)
        """
        response = requests.get(url)
        place_json = response.json()
        place, create = Place.objects.get_or_create(title=place_json['title'],
                                    description_short=place_json['description_short'],
                                    description_long=place_json['description_long'],
                                    lng=place_json['coordinates']['lng'],
                                    lat=place_json['coordinates']['lat']
                                    )
        
        image_urls = place_json['imgs']
                                                             
        for number, url in enumerate(image_urls, 1):
            #print(f'Here is the URL: {url}')
            response = requests.get(url)
            response.raise_for_status()
            img_name = url.split('/')[-1]
            #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            BASE_DIR = os.getcwd()
            img_with_path = os.path.join(BASE_DIR, 'media', 'media', img_name)
            placeimage, create = PlaceImage.objects.get_or_create(place=place, number=number)
            img_byte = BytesIO(response.content)

            placeimage.image.save(img_with_path, files.File(img_byte), save=True)
