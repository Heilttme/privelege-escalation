FROM php:8.1-apache

WORKDIR /var/www/html

COPY src/ /var/www/html/

RUN mkdir -p /var/www/html/logs

RUN chown -R www-data:www-data /var/www/html/logs && \
    chmod -R 755 /var/www/html/logs

RUN mkdir -p /var/www/data

RUN echo "user2:SuperSecurePassword" > /var/www/data/credentials.txt && \
    echo "ctfplayer:SuperSecureP@ssw0rd!" >> /var/www/data/credentials.txt

RUN chown -R www-data:www-data /var/www/data

RUN apt update && apt install -y grep

EXPOSE 80

