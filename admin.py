from django.contrib import admin

from viewer.models import Individuals, Samples


class IndividualsAdmin(admin.ModelAdmin):
    model = Individuals
    list_display = ('individual_id', 'gender')

class SamplesAdmin(admin.ModelAdmin):
    model = Samples
    list_display = ('sample_id', 'date_obtained')

admin.site.register(Individuals, IndividualsAdmin)