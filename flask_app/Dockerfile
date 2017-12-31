From alpine:latest

RUN apk add --no-cache --update python py-pip bash

ADD ./requirments.txt /app/src/requirments.txt

RUN pip install --no-cache-dir -q -r /app/src/requirments.txt

#copy my app into container's folder

ADD ./ /app/src/

WORKDIR /app/src/

RUN adduser -D myuser
USER myuser

#alternative to Expose
CMD gunicorn --bind 0.0.0.0:PORT:wsqi