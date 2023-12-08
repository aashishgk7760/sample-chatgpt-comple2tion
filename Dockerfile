FROM --platform=linux/amd64 python:3.8-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 80
ENV NAME OPENAI_API_KEY= ""
ENTRYPOINT ["python", "app.py", "--host=0.0.0.0", "--port=80"]