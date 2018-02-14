from import_export import resources
from .models import Pages


class PagesResource(resources.ModelResource):
    class Meta:
        model = Pages
        fields = ('site__name', 'url', 'found_date_time', 'last_scan_date')
