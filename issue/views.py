from django.shortcuts import render
from .models import Issue
from django.views.generic.detail import DetailView

def summary_issue_view(request):
    return render(request, 'summary_issue.html', {'issue': Issue.objects.all()})

class IssueDetailView(DetailView):
    queryset = Issue.objects.all()
    context_object_name = 'object'
    template_name = 'issue.html'