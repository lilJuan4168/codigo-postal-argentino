
FROM ubuntu

#work directory
WORKDIR /codigoPostal

#install dependencies
COPY . .
RUN apt update -y && apt upgrade -y && apt install python3-pip -y
RUN pip install -r requirements2.txt

#run
CMD ["bash_scripts/api_activate.sh"]