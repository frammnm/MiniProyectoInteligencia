from django.shortcuts import render
from django.http import  HttpResponse
from tweets.models import Tweets
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse(serializers.serialize("json",Tweets.objects.all()))

def get(request, id):
    return HttpResponse(serializers.serialize("json",Tweets.objects.filter(id=id)))