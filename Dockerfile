FROM python:3.10.2-slim-bullseye

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./config ./config

CMD ["export", "APP_CONFIG=/config/local.env"]
CMD ["printenv", "APP_CONFIG"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
