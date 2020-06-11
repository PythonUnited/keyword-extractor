FROM python:3.8

ADD . /app

WORKDIR /app

RUN CFLAGS="-Wno-narrowing" pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install gunicorn

EXPOSE 5000

RUN echo `pwd`
RUN ls -l

CMD gunicorn --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info

