FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000

CMD ["gunicorn", "categoriesAPI.wsgi:application", "--bind", "0.0.0.0:8000"]
