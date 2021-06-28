FROM python:3.8-buster
ADD checker.py .
ADD . .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./checker.py"]