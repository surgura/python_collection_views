#!/bin/sh

cd "$(dirname "$0")"

pyflakes ../../collection_views ../../tests
