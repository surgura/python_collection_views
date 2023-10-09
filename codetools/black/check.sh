#!/bin/sh

cd "$(dirname "$0")"

black --diff --check ../../collection_views ../../tests
