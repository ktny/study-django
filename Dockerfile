FROM python:3.11.0-bullseye
ENV PYTHONBUFFERED=1

COPY mysite/pyproject.toml* mysite/poetry.lock* ./

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install
