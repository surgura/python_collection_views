#!/bin/sh

cd "$(dirname "$0")"

pydocstyle ../../collection_views ../../tests
