FROM python:3.8.8

RUN apt-get update && apt-get install -y --no-install-recommends vim wget apt-utils

RUN wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
    python get-poetry.py --yes && \
    rm get-poetry.py
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml /setup/
COPY ./poetry.lock /setup/

WORKDIR /setup
RUN poetry install

WORKDIR /
CMD ["/bin/bash"]
