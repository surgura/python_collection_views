#!/bin/sh

cd "$(dirname "$0")"

darglint -s sphinx ../../collection_views ../../tests
