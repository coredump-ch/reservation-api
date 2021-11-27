# Docker image for the Reservation API.
#
# Please set the following env vars:
#
# - SECRET_KEY=...
# - DATABASE_URL='postgres://<postgres-host>/<database-name>'
# - ALLOWED_HOST='reservations.coredump.ch'
#
# See docker-compose.yml as an example on how to run this image.

FROM docker.io/python:3.9-slim-bullseye

# Add requirements file
ADD requirements.txt /code/requirements.txt
WORKDIR /code

# Install dependencies
RUN apt-get update -qq \
 && apt-get install -yq --no-install-recommends \
    dumb-init \
 && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

# Add code
ADD . /code

# Set env vars
ENV DJANGO_DEBUG=False

# Volumes
VOLUME ["/code/static/", "/code/media/"]

# Port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s \
    CMD python /code/docker/healthcheck.py

# Entry point
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/bin/bash", "docker/entrypoint.sh"]
