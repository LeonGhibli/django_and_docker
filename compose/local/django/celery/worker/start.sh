#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A django_and_docker.taskapp worker -l INFO
