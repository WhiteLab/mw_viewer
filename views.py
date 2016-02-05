import json
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import *
# Create your views here.
def mw_viewer(request):
    return render(request, 'viewer/mw_viewer_home.html')

def individual_view(request):
    ind = Individual.objects.all()
    context = {'individual': ind}
    return render(request, 'viewer/individuals/view_individual.html', context)

def individual_submit(request):
    ind = Individual.objects.all()
    context = {'individual': ind}
    return render(request, 'viewer/individuals/individual_submit.html', context)

def individual_upload(request):
    # ind = Individual.objects.all()
    # context = {'individual': ind}
    return render(request, 'viewer/individuals/individual_submit.html')

def sample_view(request):
    samp = Sample.objects.all()
    context = {'sample': samp}
    return render(request, 'viewer/samples/view_sample.html', context)

def experiment_view(request):
    exp = ExperimentDetail.objects.all()
    context = {'experiment': exp}
    return render(request, 'viewer/experiments/view_experiment.html', context)