FROM python:3.12.0-alpine3.18
RUN mkdir /python_scripts
WORKDIR /python_scripts

# docker build -t python_scripts:1.0 .
# docker run -d -it --name docker-python -v /C/Users/adolfo/Desktop/python_scripts:/python_scripts python_scripts:1.0