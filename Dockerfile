# Image python de base
FROM python:3.9-slim

# Define the working directory
WORKDIR /code

# Copy requerements (dependancies)
COPY ./requirements.txt /code/requirements.txt

# Install dependancies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY . /code/app

# Run commande to start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
