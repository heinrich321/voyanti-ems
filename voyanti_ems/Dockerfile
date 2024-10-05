# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM


# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip python3-dev libffi-dev build-base cmake g++ make patchelf pkgconfig musl-dev

RUN pip install numpy==1.21.0

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