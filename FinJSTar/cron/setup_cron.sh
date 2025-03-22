#!/bin/sh
# Создаём PID-директорию для cron
mkdir -p /var/run/cron
chown root:root /var/run/cron

# Запускаем cron в foreground
/usr/sbin/cron -f -L /var/log/cron.log

