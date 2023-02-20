import asyncio
import time

from django.http import HttpResponse

# from .models import Choice

# def index(request):
#     # time.sleep(5)
#     return HttpResponse("Hello world")


async def index(request):
    # time.sleep(5)

    # choice = Choice.objects.first()
    # assert choice
    # ans = choice.votes + 1
    # print(ans)

    return HttpResponse("Polls index")


async def hello(request):
    task = asyncio.create_task(sleep())
    await task
    return HttpResponse("Hello world")


async def sleep():
    await asyncio.sleep(3)
