from django.shortcuts import render, redirect
from .models import Issue, Message
from django.views.generic.detail import DetailView
from .forms import MessageForm

def summary_issue_view(request):
    return render(request, 'summary_issue.html', {'issue': Issue.objects.all()})

class IssueDetailView(DetailView):
    queryset = Issue.objects.all()
    context_object_name = 'object'
    template_name = 'issue.html'

def issue_view(request, pk):
    issue = Issue.objects.get(id=pk)
    message = Message.objects.filter(issue=pk).order_by('-time')
    form = MessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = request.user
            new_message.issue = issue
            new_message.save()
            return redirect ('/issue/%d' % pk)
    else:
        form = MessageForm()
    return render(request, 'issue.html', {'form': form, 'message': message, 'issue': issue.title})