# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM


# Install requirements for add-on
# Install Python 3, pip, numpy, and necessary build tools
RUN apk add --no-cache python3 py3-pip python3-dev libffi-dev build-base cmake g++ make patchelf pkgconfig musl-dev \
    && apk add --no-cache py3-numpy

RUN pip freeze
RUN python3 --version


# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Copy root filesystem
COPY rootfs /

RUN pip install -r /usr/src/requirements.txt