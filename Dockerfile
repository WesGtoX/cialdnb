FROM python:3.10.5-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-m", "run_cialdnb"]
