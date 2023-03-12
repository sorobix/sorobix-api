FROM python:3.11-slim-buster
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 3001
CMD ["python","wsgi.py"]
