import asyncio

from django.http import HttpResponse

from .models import Choice

# import time


# def index(request):
#     # time.sleep(5)
#     return HttpResponse("Hello world")


def arerare(a: int, b: int) -> int:
    return a + b


async def index(request):
    # time.sleep(5)

    choice = Choice.objects.first()
    assert choice
    ans = choice.votes + 1
    ans = "aaa"

    print(ans)

    return HttpResponse("Polls index")


async def hello(request):
    task = asyncio.create_task(sleep())
    await task
    return HttpResponse("Hello world")


async def sleep():
    await asyncio.sleep(3)
