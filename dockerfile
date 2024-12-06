# Use an image that includes both Python and Chrome
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install allure-pytest and webdriver-manager
RUN pip install allure-pytest webdriver-manager

# Run your tests
CMD ["pytest", "-v", "-s", "./playwrighttests", "-m", "VideoGen", "--alluredir=./reports/allure-results", "--env", "dev"]
