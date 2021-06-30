FROM python:3.8-buster
ADD . .
RUN pip install -r requirements.txt
CMD ["./checker_api.py"]
ENTRYPOINT ["python"]