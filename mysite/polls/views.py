import time

from django.http import HttpResponse

# def index(request):
#     # time.sleep(5)
#     return HttpResponse("Hello world")


async def index(request):
    # time.sleep(5)

    return HttpResponse("Polls index")


async def hello(request):
    time.sleep(5)

    return HttpResponse("Hello world")
