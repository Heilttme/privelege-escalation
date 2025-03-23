FROM debian:latest

RUN apt update && apt install -y \
    openssh-server \
    sudo \
    vim \
    less \
    coreutils \
    findutils \
 && mkdir /var/run/sshd

RUN useradd -m -s /bin/bash user2 && \
    echo "user2:securepassword" | chpasswd

RUN echo "user2 ALL=(ALL) NOPASSWD: /usr/bin/less, /usr/bin/tail, /usr/bin/find, /usr/bin/vim" > /etc/sudoers.d/user2 && \
    chmod 440 /etc/sudoers.d/user2

RUN echo "SSBnYXZlIHlvdSBwZXJtaXNzaW9uIHRvIGV4ZWN1dGUgc29tZSBvZiBjb21hbmRzIGZvciByZWFkaW5nIGZpbGVzIHNvIHlvdSBtaWdodCB3YW50IHRvIGNoZWNrIHRoZW0gb3V0LiBCdXQgeW91IHN0aWxsIHdvbid0IGJlIGFibGUgdG8gcmVhZCB0aGUgZmxhZyBpbiAvcm9vdC9yb290LnR4dCBoYS1oYS4=" > /home/user2/README.txt && \
    chown user2:user2 /home/user2/README.txt

RUN echo "practice{h@h_u_2_g0od_fr}" > /root/root.txt && chmod 600 /root/root.txt

RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

