from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def health(request):
    return JsonResponse(data={"message": "app is up and running"})
