ARG PYTHON_VERSION=3.8
FROM python:$PYTHON_VERSION as build

# setup workspace and user for application
ARG APP_USER=appuser

RUN mkdir /workspace && \
useradd -m -u 1000 $APP_USER && \
chmod 777 -R /usr/local /workspace

USER $APP_USER

# upgrade pip
RUN pip install --upgrade pip

# install poetry - python dependency manager
ARG POETRY_VERSION=1.2.0
ENV POETRY_HOME="/usr/local/poetry"
RUN curl -sSL https://install.python-poetry.org | python - --version $POETRY_VERSION \
&& ln -sf "$POETRY_HOME"/bin/poetry /usr/local/bin/poetry \
&& poetry --version

# inject application files
ADD --chown=$APP_USER ./ /workspace

WORKDIR /workspace

RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn",  "app.main:app"]
#ENTRYPOINT [ "tail", "-f", "/dev/null"] # debug container purpose

CMD ["--host=0.0.0.0", "--port=8000"]