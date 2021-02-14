from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project, Member, Report, Chat
from django.views.generic.detail import DetailView
from .forms import ChatForm
import requests, json


def summary_project_view(request):
    return render(request, 'summary_project.html', {'project': Project.objects.all()})

class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    context_object_name = 'project'
    template_name = 'project.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_no_sorted = Chat.objects.all()
        chat_sorted = chat_no_sorted.order_by('-time')
        context['chat'] = chat_sorted
        return context

def project_chat_view(request, pk):
    project = Project.objects.get(id=pk)
    chat = Chat.objects.filter(project=pk).order_by('-time')
    form = ChatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = request.user
            new_message.project = project
            new_message.save()
            return redirect ('/project/%d/chat' % pk)
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

def summary_opendata_view(request):
    return render(request, 'summary_opendata.html')

def project_opendata_view(request, fed_project):
#    get_project_json = requests.get('http://budget.gov.ru/epbs/registry/7710168360-REGIONALPROJECT/data?filtersubject.code=86&filterfpcode=' + fed_project)
    header = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection':'keep-alive',
                'Host':'budget.gov.ru',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
                }

    proxi = {
                 'http': '154.16.202.22:8080'
                }

    url = 'http://budget.gov.ru/epbs/registry/7710168360-REGIONALPROJECT/data?filtersubject.code=86&filterfpcode=F1'
    get_project_json = requests.get(url, headers=header, proxies=proxi)

#    get_project_json_text = json.loads(get_project_json.text)
    get_project_json_text = get_project_json
#    code = get_project_json_text['data']['0']['code']
#    fullname = get_project_json_text['data']['0']['fullname']
#    curator = get_project_json_text['data']['0']['curator']
#    person = get_project_json_text['data']['0']['person']
#    kvsr = get_project_json_text['data']['0']['kvsr']
#    return render(request, 'project_opendata.html', {'code': code, 'fullname': fullname, 'curator': curator, 'person': person, 'kvsr': kvsr})

    return render(request, 'project_opendata.html', {'get_project_json_text': get_project_json_text})




