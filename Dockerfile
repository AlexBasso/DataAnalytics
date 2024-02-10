FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app4

RUN pip install --upgrade pip "poetry==1.7.1"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN apt-get update && apt-get install -y git
RUN poetry install

COPY dataanalytics .

CMD ["gunicorn", "dataanalytics.wsgi:application", "--bind", "0.0.0.0:8003"]