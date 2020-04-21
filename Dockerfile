FROM python:3.6.10-alpine


# COPIANDO ARCHIVOS.

RUN mkdir -p /app
WORKDIR /app
COPY . .

# RUN pip install -r requirements.txt

CMD python app.py
