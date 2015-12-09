from django.contrib import admin

from models import Individual, Sample, ExperimentDetail


class IndividualAdmin(admin.ModelAdmin):
    model = Individual
    list_display = ('individual_id', 'gender')
class SampleAdmin(admin.ModelAdmin):
    model = Sample
    list_display = ('sample_id', 'date_obtained', 'tissue', 'individual')

class ExperimentAdmin(admin.ModelAdmin):
    model = ExperimentDetail
    list_display = ('date', 'duration', 'pipetting', 'gels', 'electrophoresis', 'transfer', 'comments', 'sample')

admin.site.register(Individual, IndividualAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(ExperimentDetail, ExperimentAdmin)