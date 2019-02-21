from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# 返回字节流
def index(request):
    return HttpResponse("Hello, world")


# 返回JSON
def json(request):
    return JsonResponse({"msg": "Hello,world"})


# 返回HTML
def home(request):
    return render(request, 'blog/index.html')

