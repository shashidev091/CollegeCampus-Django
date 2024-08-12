from django.shortcuts import render

from .models import College
from User.models import User
# Create your views here.

def all_colleges(request):
    users = User.objects.all()
    list_of_users = list(users)
    print(list_of_users)
    colleges = College.objects.all()
    list_of_colleges = list(colleges)
    print(list_of_colleges)
    return render(request=request, template_name='collegedetails/index.html', context={
        "colleges": list_of_colleges
    })


def home(request):

    return render(request=request, template_name="collegedetails/collegeList.html", context={})