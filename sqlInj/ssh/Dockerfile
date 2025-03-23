FROM ubuntu:20.04

RUN apt-get update && apt-get install -y openssh-server sudo

RUN useradd -m -d /home/ctf-user -s /bin/bash ctf-user \
    && echo "ctf-user:SuperSecureP@ssw0rd!" | chpasswd

RUN mkdir /var/run/sshd

RUN ssh-keygen -A

RUN mkdir -p /root/.ssh;
RUN touch /root/.ssh/authorized_keys;
RUN touch /home/ctf-user/user.txt
RUN echo "practice{Y0u_MAD3_1T_K1ND4_F4R}" > /home/ctf-user/user.txt
RUN echo "practice{Y0u_MAD3_1T_TH4T_F4R_T0_R00T}" > /root/root.txt

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN echo "ctf-user ALL=(ALL) NOPASSWD: /usr/bin/tee" > /etc/sudoers.d/ctf-user

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

