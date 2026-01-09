FROM python:3.14.2

# host.docker.internal -> localhost of host machine
# curl -X POST -d '{message: "Hello"}' -H "Content-Type: application/json" http://host.docker.internal:8000/api/chats/
RUN apt-get update && apt-get install -y curl

RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

# COPY local_folder/file container_destination_folder/file
COPY requirements.txt /tmp/requirements.txt

# Run within container while building the image
RUN pip install -r /tmp/requirements.txt
# /opt/venv/bin/pip install --upgrade pip
COPY ./src .

CMD ["python", "-m", "http.server", "8000"] 
