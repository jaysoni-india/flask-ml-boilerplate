# base image
FROM python:3.10

# set the working directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
