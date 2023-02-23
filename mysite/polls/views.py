import asyncio

from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from django.core import serializers
from django.http import HttpRequest, HttpResponse

from .models import Choice, Question

# from rest_framework.decorators import api_view


async def index(request: HttpRequest):
    return HttpResponse("Polls index")


async def list(request: HttpRequest):
    questions = []
    async for question in Question.objects.all():
        questions.append(question)

    return HttpResponse(
        serializers.serialize("json", questions),
        content_type="application/json; charset=utf-8",
    )


async def hello(request: HttpRequest):
    task = asyncio.create_task(sleep())
    await task
    return HttpResponse("Hello world")


async def sleep():
    await asyncio.sleep(3)


# @sync_to_async
# @api_view(["GET"])
# def drf(request: HttpRequest):
#     if request.method == "GET":
#         return HttpResponse("hello drf")


@api_view(["GET", "POST"])
async def drf(request: HttpRequest):
    if request.method == "GET":
        return HttpResponse("hello drf")
    elif request.method == "POST":
        question = await Question.objects.afirst()
        assert question is not None
        return HttpResponse(question.question_text)
