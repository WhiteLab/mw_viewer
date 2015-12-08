from django.contrib import admin

from models import Individual, Sample


class IndividualAdmin(admin.ModelAdmin):
    model = Individual
    list_display = ('individual_id', 'gender')
class SampleAdmin(admin.ModelAdmin):
    model = Sample
    list_display = ('sample_id', 'date_obtained', 'tissue', 'individual')

admin.site.register(Individual, IndividualAdmin)
admin.site.register(Sample, SampleAdmin)