FROM alpine:latest
RUN apk update
RUN apk add python3 py3-pip
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip3 install flask flask-restful
RUN mkdir /app
COPY ./app.py /app/app.py
#execute when cntainer has run
CMD python3 /app/app.py
