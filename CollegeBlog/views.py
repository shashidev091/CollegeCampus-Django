from django.shortcuts import render

# Create your views here.


def landing_page(request):
    print("Landing Page")
    return render(request=request, template_name='collegeBlog/index.html', context={
        "title": "CollegeCampus | Search you Dream College here",
        "author": "Shashi Bhagat"
    })