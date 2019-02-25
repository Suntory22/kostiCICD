FROM alpine:3.8.1 
RUN apk add --update python py-pip 
COPY requirements.txt /src/requirements.txt 
RUN pip install -r /src/requirements.txt 
COPY app.py /src 
COPY kostiP /src/kostiP
COPY static /src/static
COPY templates /src/templates
COPY __init.py__ /src 
CMD python /src/app.py
