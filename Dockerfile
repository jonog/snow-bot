FROM python:3.9-slim-bullseye
COPY ./requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY . .
CMD ["python", "app.py"]