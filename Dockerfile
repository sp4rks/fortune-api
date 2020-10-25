FROM python:3-slim

WORKDIR /opt/fortune-api

COPY requirements.txt ./
RUN apt update -y
RUN apt install fortune-mod -y
RUN ln -s /usr/games/fortune /usr/local/bin/fortune
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./fortune-api.py" ]
