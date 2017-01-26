from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    n = request.POST['name']
    d = request.POST['desc']
    Course.objects.create(name=n, desc=d)
    return redirect('/')

def show_confirm(request,id):
    context = {
        'id': id,
        'name': Course.objects.get(id=id).name,
        'desc': Course.objects.get(id=id).desc
    }
    return render(request, 'courses_app/confirm.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
