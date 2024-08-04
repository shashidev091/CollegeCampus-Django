from django.shortcuts import render

# Create your views here.

def all_colleges(request):
    colleges = []
    return render(request=request, template_name='collegedetails/index.html', context={})


def home(request):
    return render(request=request, template_name="collegedetails/index.html", context={})