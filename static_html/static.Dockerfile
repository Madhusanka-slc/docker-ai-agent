FROM python:3.14.2

WORKDIR /app

# COPY local folder -> container folder
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

COPY ./src .

# RUN echo "hello world from Dockerfile" > index.html

# docker build -f Dockerfile -t pyapp .
# docker run -it --rm pyapp

# docker build -f Dockerfile -t madhusankaslc/ai-py-app-test:latest .
# docker push madhusankaslc/ai-py-app-test:latest

# docker run -it --rm -p 3000:8000 pyapp
# docker run -it -p 8000:8000 pyapp

# python -m http.server 8000
CMD ["python", "-m", "http.server", "8000"] # default command to run the server
