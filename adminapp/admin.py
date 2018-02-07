from django.contrib import admin
from .models import Persons, PersonPageRank, Keywords, Pages, Sites


admin.site.register(Persons)
admin.site.register(PersonPageRank)
admin.site.register(Keywords)
admin.site.register(Pages)
admin.site.register(Sites)
