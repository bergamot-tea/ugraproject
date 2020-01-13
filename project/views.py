from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project, Member, Report, Chat
from django.views.generic.detail import DetailView
from .forms import ChatForm


def summary_project_view(request):
    return render(request, 'summary_project.html', {'project': Project.objects.all()})

class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    context_object_name = 'project'
    template_name = 'project.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_no_sorted = Chat.objects.all()
        chat_sorted = chat_no_sorted.order_by('-date_post')
        context['chat'] = chat_sorted
        return context

def project_chat_view(request, pk):
    project = Project.objects.get(id=pk)
    chat = Chat.objects.filter(project=pk).order_by('-date_post')
    form = ChatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.project = project
            message.save()

    else:
        form = ChatForm()
    return render(request, 'project_chat.html', {'form': form, 'chat': chat, 'project': project.name})


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
