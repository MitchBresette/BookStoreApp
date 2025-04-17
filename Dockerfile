# Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code and .env file into the container
COPY . /app

# Expose port for the app
EXPOSE 8080

# Set Flask environment to production
ENV FLASK_ENV=production

# Run the app when the container starts
CMD ["python", "app.py"]