__author__ = 'Miguel Brown'

from django import forms
from models import Individual
from models import Sample

class IndividualForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Individual
        fields = ['individual_id', 'gender']