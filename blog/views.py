from django.http import HttpResponse


def hello_blog(request):
    return HttpResponse("Hello, blog!")
