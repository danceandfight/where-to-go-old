from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage
from adminsortable2.admin import SortableInlineAdminMixin

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width = 'auto',
            height = '200',
            )
    )

    fields = ('image', 'place', 'image_preview', 'number')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]

admin.site.register(PlaceImage)