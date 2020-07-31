from django.contrib import admin
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
	model = PlaceImage
	ordering = ('number',)

class PlaceAdmin(admin.ModelAdmin):
	inlines = [
	    PlaceImageInline,
	]

class PlaceImageAdmin(admin.ModelAdmin):
	ordering = ('number',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)