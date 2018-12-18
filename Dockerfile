FROM python:3.6-stretch
ENV PYTHONBUFFERED 1

WORKDIR /chat
COPY server.py /chat/

EXPOSE 8888/udp
CMD ["python", "/chat/server.py"]
