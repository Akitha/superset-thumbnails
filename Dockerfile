FROM apache/superset:1.0.1
USER root
RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod +x chromedriver && \
    mv chromedriver /usr/bin && \
    apt autoremove -yqq --purge && \
    apt clean && \
    rm -f google-chrome-stable_current_amd64.deb chromedriver_linux64.zip
RUN pip install --no-cache-dir gevent
RUN pip install --no-cache-dir mysqlclient
RUN pip install --no-cache-dir psycopg2
RUN pip install --no-cache-dir redis
RUN pip install --no-cache-dir flower
USER superset
