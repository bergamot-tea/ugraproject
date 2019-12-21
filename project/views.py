from django.shortcuts import render
from .models import Project


def summary_view(request):
    return render(request, 'summary.html', {'project': Project.objects.all()})