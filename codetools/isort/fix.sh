#!/bin/sh

cd "$(dirname "$0")"

isort --profile black ../../collection_views ../../tests
