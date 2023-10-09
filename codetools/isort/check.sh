#!/bin/sh

cd "$(dirname "$0")"

isort --check-only --diff --profile black ../../collection_views ../../tests
