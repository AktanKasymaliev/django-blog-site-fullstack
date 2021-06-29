from django.shortcuts import render
from django.template import RequestContext

def handler404(request, *args, **kwargs):
    return render(request, 'errors/404.html', {},  status=404)