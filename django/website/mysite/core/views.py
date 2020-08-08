from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from subprocess import run, PIPE
import sys
# from .forms import BookForm
# from .models import Book


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #when receive 'document' file
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(context['url'])
        out = run([sys.executable, 'C://Users//user//Desktop//jh//model//test.py', context['url']], shell = False, stdout=PIPE)
        context['out']=out.stdout.decode()
        print(context['out'])
    return render(request, 'upload.html', context)
