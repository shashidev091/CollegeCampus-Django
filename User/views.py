from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Avg
from . import utils


# Create your views here.


def get_users(request):
    users = utils.get_users()
    return JsonResponse({
        "page": "Users page",
        "User": [user.get_dict() for user in users]
    })


def add_users(request):
    # utils.seed_user()
    return render(request, template_name='users/index.html', context={
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


def dynamic_path(request, month):
    return HttpResponse(f"Some dynamic path accessed: {month}")


def dynamic_path_int(request, month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'july', 'August', 'September', 'October',
              'November', 'December']
    try:
        month_name = months[month - 1]
        return HttpResponseRedirect(reverse('dynamic_path', args=[month_name]))
        # return HttpResponse(f"Some dynamic path accessed: {month_name}")
    except:
        print("Here")
        raise Http404()


def user_detail(request, id):
    return HttpResponse(f"user with name {id}")