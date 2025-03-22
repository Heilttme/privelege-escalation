FROM python:3.9

RUN apt update && apt install -y --no-install-recommends \
    nodejs npm cron gosu tar && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user1

WORKDIR /opt/app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN npm install -g safe-eval

COPY app/ .

COPY cron/cronjob /etc/cron.d/tar_job
COPY cron/setup_cron.sh /setup_cron.sh
RUN chmod 644 /etc/cron.d/tar_job
RUN chmod +x /setup_cron.sh

RUN chmod +x /setup_cron.sh && \
    mkdir -p /backup /var/logs && \
    chown user1:user1 /var/logs /backup && \
    mkdir -p /var/run/cron && \
    chown root:root /var/run/cron

RUN echo "Log file 1" > /var/logs/log1.txt && \
    echo "Log file 2" > /var/logs/log2.txt && \
    echo "Log file 3" > /var/logs/log3.txt && \
    chown user1:user1 /var/logs/log*

# Инициализация cron (от root)
RUN crontab /etc/cron.d/tar_job

# Настройка окружения
RUN touch /var/log/cron.log && \
    chmod 644 /var/log/cron.log && \
    chown root:root /var/log/cron.log

# Флаги
RUN echo "flag{this_is_user1_flag}" > /home/user1/user.txt && \
    chmod 444 /home/user1/user.txt

# Запуск cron от root и Flask от user1
CMD ["bash", "-c", "/setup_cron.sh && exec gosu user1 flask run --host=0.0.0.0 --port=5000"]

