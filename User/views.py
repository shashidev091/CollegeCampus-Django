from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def home(request):
    return JsonResponse({
        "page": "Users page",
        "User": []
    })


def home_temp(request):
    return render(request, template_name='pages/index.html', context={
        "title": "College Campus",
        "colleges": [
            "Indian Institute of Technology (IIT) Dhanbad",
            "Birla Institute of Technology Mesra (BIT Mesra)",
            "Xavier Institute of Social Service (XISS Ranchi)",
            "Indian Institute of Management (IIM) Ranchi",
            "National Institute of Technology (NIT) Jamshedpur",
            "Ranchi University, Ranchi",
            "Sidhu Kanhu Murmu University, Dumka",
            "Binod Bihari Mahto Koyalanchal University, Dhanbad"
        ]
    })
