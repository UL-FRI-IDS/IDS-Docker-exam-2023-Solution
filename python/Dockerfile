FROM python:3.12-bookworm

WORKDIR /data

ENV DATA_DIR '/data'
ENV JUPYTER_PASSWORD 'Geslo.01'

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 8888

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser \
            --NotebookApp.token=${JUPYTER_PASSWORD} --allow-root --notebook-dir=${DATA_DIR}