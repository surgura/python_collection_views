#!/bin/sh

set -e

cd "$(dirname "$0")"
INI=$(pwd)/mypy.ini
cd "../.."

mypy --config-file $INI --package collection_views
mypy --config-file $INI --package tests
