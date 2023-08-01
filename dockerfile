
FROM python:3.11.3

#work directory
WORKDIR /codigoPostal

#install dependencies
COPY requirements2.txt api.py credentials.json /codigoPostal/
RUN pip install --upgrade pip ; pip install -r requirements2.txt


#run
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]