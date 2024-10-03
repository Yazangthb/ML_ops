FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt 

EXPOSE 8000

CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
