from django.shortcuts import render
from .models import Health

def index(request):
    return render(request, 'index.html')

def chart(request):
    Health_list = Health.objects.filter(staff_no=21850)
    return render(request, 'chart.html', {'Health_list': Health_list})
