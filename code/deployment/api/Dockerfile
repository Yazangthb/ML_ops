FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip

WORKDIR /api

COPY ./deployment/api/ . 

COPY ../../models/model.pkl /api/models/model.pkl

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt 

EXPOSE 8001

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]
