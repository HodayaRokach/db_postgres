FROM python:3.12
USER root
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "src/app.py"]


