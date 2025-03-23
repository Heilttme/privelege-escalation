FROM docker:dind

RUN apk add --no-cache openssh sudo shadow bash iptables fail2ban tzdata procps

RUN ssh-keygen -A

ENV USERNAME="ctfplayer"
ENV PASSWORD="SuperSecureP@ssw0rd!"

RUN adduser -h /home/$USERNAME -s /bin/bash -D $USERNAME

RUN echo "$USERNAME:$PASSWORD" | chpasswd

RUN addgroup $USERNAME docker

RUN echo "practice{d0ck3r_pr1v_3sc_1nt3rm3d14te}" > /home/$USERNAME/user.txt
RUN echo "practice{d0ck3r_pr1v_3sc_m4st3r}" > /root/root.txt
RUN chmod 600 /root/root.txt

RUN echo "$USERNAME ALL=(ALL) /bin/cat, !/bin/cat /root/*, !/bin/cat /*flag*" > /etc/sudoers.d/ctfplayer
RUN chmod 440 /etc/sudoers.d/ctfplayer

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#MaxAuthTries 6/MaxAuthTries 3/' /etc/ssh/sshd_config

RUN echo '#!/bin/sh' > /usr/local/bin/setup-firewall.sh && \
    echo 'iptables -A INPUT -p tcp --dport 2222 -j ACCEPT' >> /usr/local/bin/setup-firewall.sh && \
    echo 'iptables -A INPUT -i lo -j ACCEPT' >> /usr/local/bin/setup-firewall.sh && \
    echo 'iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT' >> /usr/local/bin/setup-firewall.sh && \
    chmod +x /usr/local/bin/setup-firewall.sh

EXPOSE 22

CMD ["sh", "-c", "/usr/local/bin/setup-firewall.sh; ssh-keygen -A && dockerd & exec /usr/sbin/sshd -D"]

