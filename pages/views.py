from django.shortcuts import render,redirect

from .models import Issue,Assignment

from users.models import Profile

from .forms import IssueForm
# Create your views here.
from django.contrib import messages


def home_view(request):
    context={
        'agents':Profile.objects.all(),
        'issues':Issue.objects.all(),
        'assignments':Assignment.objects.all(),
        'issue_form':IssueForm(),
    }

    if request.method == 'POST':
        form=IssueForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,"Issue Created")
            return redirect('home')
    else :
        form=IssueForm()
    return render(request,'pages/home.html',context)
def delete_view(request,pk):
    AM = Assignment.objects.get(id=pk)
    messages.success(request,"Assignment deleted, agent "+str(AM.agent) + " is available now." )
    AM.delete()
    return redirect('home')
