FROM python:3.11.0-bullseye
WORKDIR /opt
ENV PYTHONPATH /opt

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.in-project true

COPY ./mysite/pyproject.toml ./mysite/poetry.lock ./
RUN poetry install

ENTRYPOINT ["./entrypoint.sh"]
