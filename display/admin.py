from django.contrib import admin

from django.contrib import admin
from display.models import Protein, Sea, Sequence

# Register your models here.
admin.site.register(Sea)
admin.site.register(Sequence)
admin.site.register(Protein)