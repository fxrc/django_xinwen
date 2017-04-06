from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Title

def index(request):
    return render(request,'xinwen/index.html')

def titles(request):
    titles = Title.objects.all()
    context = {'titles':titles}
    return render(request,'xinwen/titles.html',context)

def title(request,title_id):
    title = Title.objects.get(id=title_id)
    content = title.content_set.all()
    context={'title':title,'contents':content}
    return render(request,'xinwen/title.html',context)

