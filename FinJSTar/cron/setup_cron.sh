#!/bin/sh
mkdir -p /var/run/cron
chown root:root /var/run/cron
/usr/sbin/cron -f -L /var/log/cron.log

