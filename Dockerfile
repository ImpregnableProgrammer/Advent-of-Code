FROM arm64v8/ubuntu:kinetic
LABEL description="Docker container for running PyPy in AMD64 ubuntu on macOS Ventura using Apple Virtualization"
SHELL ["/usr/bin/bash", "-c"]
RUN apt-get update && apt-get -y install pypy && apt-get clean