FROM python:3.7-alpine

COPY python_files/config.py /python_files/
COPY python_files/cartiReply.py /python_files/
COPY python_files/cartiMain.py /python_files/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /python_files
CMD ["python3", "cartiReply.py "]