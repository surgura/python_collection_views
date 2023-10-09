#!/bin/sh

set -e

cd "$(dirname "$0")/../.."

mypy --package collection_views
mypy --package tests
