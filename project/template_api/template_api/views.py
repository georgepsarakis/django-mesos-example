from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return redirect('/api', permanent=True)
