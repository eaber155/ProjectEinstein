from django.shortcuts import render
from .models import Staff

def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'autesha/staff_list.html', {'staff': staff})
