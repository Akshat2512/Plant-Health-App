FROM php:7.4-cli
WORKDIR /app
COPY . /app
RUN docker-php-ext-install mysqli
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install Python dependencies
COPY Python_Backend/requirements.txt /app/Python_Backend/requirements.txt
RUN pip3 install -r /app/Python_Backend/requirements.txt

CMD ["php", "-S", "0.0.0.0:8000", "-t", "/app"]