FROM python:3.9-slim

WORKDIR /app

ENV APP_VERSION="1.0.0"

RUN pip install flask

COPY src/app.py .

EXPOSE 5000

CMD ["python3", "src/app.py"]

