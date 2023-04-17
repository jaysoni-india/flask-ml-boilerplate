# base image
FROM python:3.10

# set the working directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# expose the port the app will run on
EXPOSE 5000
