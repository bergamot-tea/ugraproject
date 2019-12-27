from django.shortcuts import render
from .models import Project, Member, Report
from django.views.generic.detail import DetailView

def summary_project_view(request):
    return render(request, 'summary_project.html', {'project': Project.objects.all()})

class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    context_object_name = 'object'
    template_name = 'project.html'

def summary_member_view(request):
    return render(request, 'summary_member.html', {'member': Member.objects.all()})

class MemberDetailView(DetailView):
    queryset = Member.objects.all()
    context_object_name = 'member'
    template_name = 'member.html'

def summary_report_view(request):
    return render(request, 'summary_report.html', {'report': Report.objects.all()})

class ReportDetailView(DetailView):
    queryset = Report.objects.all()
    context_object_name = 'report'
    template_name = 'report.html'