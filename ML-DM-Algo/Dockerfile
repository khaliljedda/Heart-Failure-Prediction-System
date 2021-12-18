FROM python:3.8
WORKDIR /project
ADD . /project
RUN pip install --default-timeout=100 -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]