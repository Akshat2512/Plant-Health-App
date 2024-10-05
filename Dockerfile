# Use a base image
FROM php:7.4-apache

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN docker-php-ext-install pdo pdo_mysql

# Expose port
EXPOSE 8000