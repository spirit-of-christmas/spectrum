FROM python:3.12 AS dev
# Configure Poetry

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app/spectrum
RUN apt update -y && apt upgrade -y && apt install -y postgresql

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools wheel \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

RUN poetry config warnings.export false
# Add `poetry` to PATH

COPY . /app/spectrum
RUN poetry install && poetry lock --no-update && poetry export -f requirements.txt --output requirements.txt
RUN groupadd -r docker && useradd -r -m -g docker docker
RUN chown -R docker /opt
ENV PYTHONPATH $PYTHONPATH:/app

FROM python:3.12 AS prod

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/spectrum
RUN apt update -y && apt upgrade -y

COPY . /app/spectrum
COPY --from=dev /app/spectrum/requirements.txt .

RUN pip install -r requirements.txt
RUN groupadd -r docker && useradd -r -m -g docker docker

