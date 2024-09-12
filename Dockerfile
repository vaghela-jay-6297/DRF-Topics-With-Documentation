# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirement.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the project files into the container
COPY . /app

# Expose the port that the application will run on
EXPOSE 8000

# Run the application
CMD python manage.py runserver