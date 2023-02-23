import asyncio

from asgiref.sync import sync_to_async
from django.core import serializers
from django.http import HttpResponse

from .models import Choice, Question


async def index(request):
    return HttpResponse("Polls index")


async def list(request):
    questions = []
    async for question in Question.objects.all():
        questions.append(question)

    return HttpResponse(
        serializers.serialize("json", questions),
        content_type="application/json; charset=utf-8",
    )


async def hello(request):
    task = asyncio.create_task(sleep())
    await task
    return HttpResponse("Hello world")


async def sleep():
    await asyncio.sleep(3)
