# syntax=docker/dockerfile:experimental
FROM quay.io/unstructured-io/base-images:rocky8.7-2

# NOTE(crag): NB_USER ARG for mybinder.org compat:
#             https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html
ARG NB_USER=notebook-user
ARG NB_UID=1000
ARG PIP_VERSION
ARG PIPELINE_FAMILY


# Set up environment
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN groupadd --gid ${NB_UID} ${NB_USER}
RUN useradd --uid ${NB_UID} --gid ${NB_UID} ${NB_USER}
WORKDIR ${HOME}
RUN mkdir ${HOME}/.ssh && chmod go-rwx ${HOME}/.ssh \
  &&  ssh-keyscan -t rsa github.com >> /home/${NB_USER}/.ssh/known_hosts

ENV PYTHONPATH="${PYTHONPATH}:${HOME}"
ENV PATH="/home/${NB_USER}/.local/bin:${PATH}"

COPY requirements/base.txt requirements-base.txt
COPY requirements/dev.txt requirements-dev.txt
RUN python3.8 -m pip install pip==${PIP_VERSION} \
  && dnf -y groupinstall "Development Tools" \
  && su -l ${NB_USER} -c 'pip3.8 install  --no-cache  -r requirements-base.txt' \
  && su -l ${NB_USER} -c 'pip3.8 install  --no-cache  -r requirements-dev.txt' \
  && dnf -y groupremove "Development Tools" \
  && dnf clean all \
  && ln -s /home/notebook-user/.local/bin/pip /usr/local/bin/pip || true

USER ${NB_USER}

COPY logger_config.yaml logger_config.yaml
COPY prepline_${PIPELINE_FAMILY}/ prepline_${PIPELINE_FAMILY}/
COPY exploration-notebooks exploration-notebooks
COPY pipeline-notebooks pipeline-notebooks


RUN pip3.8 install --no-cache -r requirements-dev.txt
