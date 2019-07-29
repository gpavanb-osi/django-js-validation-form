from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
# Create your views here.


def IndexView(request):
    obj = render(request, 'index.html')
    return obj


def Registration(request):
    post = Post()
    post.userid = request.POST.get('userid')
    post.password = request.POST.get('passid')
    post.name = request.POST.get('username')
    post.address = request.POST.get('address')
    post.country = request.POST.get('country')
    post.zipcode = request.POST.get('zip')
    post.email = request.POST.get('email')
    post.sex = request.POST.get('sex')
    post.language = request.POST.get('lang')
    post.about = request.POST.get('desc')
    post.save()

    data = (userid, password,
            name, address, country,
            zipcode, email, sex,
            language, about)

    return JsonResponse(data)