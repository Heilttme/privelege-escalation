FROM python:3.7

RUN apt update && apt install -y postgresql-client

ARG project_dir=/opt/ctf_app/
WORKDIR $project_dir

COPY requirements.txt $project_dir
RUN pip install -r requirements.txt

RUN useradd -m -s /bin/bash webuser

RUN echo "DB_USER=ctf_user\nDB_PASSWORD=ctf_password\nDB_NAME=ctf_db\nDB_HOST=db" > /home/webuser/.env && \
    chown webuser:webuser /home/webuser/.env && \
    chmod 600 /home/webuser/.env

RUN echo "practice{go0d_olD_sst1}" > /home/webuser/user.txt && \
    chown webuser:webuser /home/webuser/user.txt && \
    chmod 644 /home/webuser/user.txt

COPY . $project_dir
RUN chown -R webuser:webuser $project_dir

WORKDIR /home/webuser

EXPOSE 5000

USER webuser
CMD python /opt/ctf_app/app.py

