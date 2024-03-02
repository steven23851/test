FROM python:alpine
RUN python3 -m pip install --no-cache-dir -U \
    https://github.com/steven23851/test/archive/refs/heads/master.tar.gz
ENTRYPOINT [ "test" ]
