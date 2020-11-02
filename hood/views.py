from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Business_centres, Neighbourhood, Profile
from .serializer import ProfileSerializer,NeighbourhoodSerializer,Business_centresSerializers

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')
