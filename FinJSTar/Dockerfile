FROM python:3.9

RUN apt update && apt install -y --no-install-recommends \
    nodejs npm cron gosu tar && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m webuser

WORKDIR /opt/app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN npm install -g safe-eval

COPY app/ .

COPY cron/cronjob /etc/cron.d/tar_job
COPY cron/setup_cron.sh ./setup_cron.sh
RUN chmod 0644 /etc/cron.d/tar_job && chmod +x ./setup_cron.sh

RUN mkdir -p /var/logs/backup && \
    chown webuser:webuser /var/logs /var/logs/backup && \
    mkdir -p /var/run/cron && \
    chown root:root /var/run/cron

RUN echo "Log file 1" > /var/logs/log1.txt && \
    echo "Log file 2" > /var/logs/log2.txt && \
    echo "Log file 3" > /var/logs/log3.txt && \
    chown webuser:webuser /var/logs/*

RUN crontab /etc/cron.d/tar_job

RUN touch /var/log/cron.log && \
    chmod 644 /var/log/cron.log && \
    chown root:root /var/log/cron.log

RUN echo "Don't forget to check the archived logs, they're being made once every minute." > /home/webuser/readme.txt && \
    chmod 644 /home/webuser/readme.txt && \
    chown webuser:webuser /home/webuser/readme.txt

RUN echo "flag{EVIL_JORDAN}" > /home/webuser/user.txt && \
    chmod 444 /home/webuser/user.txt

RUN echo "flag{cant_believe_y0u_have_m4de_it_this_f4r}" > /root/root.txt && \
    chmod 444 /root/root.txt

CMD ["bash", "-c", "./setup_cron.sh && exec gosu webuser flask run --host=0.0.0.0 --port=5000"]

