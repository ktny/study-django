import asyncio
from logging import getLogger

from adrf.decorators import api_view

# from asgiref.sync import sync_to_async
from django.db import transaction
from django.http import HttpRequest, HttpResponse

from .database import get_data_from_asyncpg
from .models import Question

logger = getLogger(__name__)


async def index(request: HttpRequest):
    return HttpResponse("Polls index")


@transaction.non_atomic_requests
@api_view(["GET"])
async def polls(request: HttpRequest):
    logger.info("start polls")

    # asyncpgを使用してraw sqlでDBのI/O待ちで並行処理を行えることを確認する
    result = await get_data_from_asyncpg()

    # django ormのネイティブなacountなどのメソッドでDBのI/O待ちで並行処理が行えることを確認する
    # result = await get_data_from_django_orm()
    return HttpResponse(result, content_type="application/json; charset=utf-8")


async def get_data_from_django_orm():
    logger.info("start get_count")
    c = await Question.objects.acount()
    await asyncio.sleep(1.0)
    return c


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
