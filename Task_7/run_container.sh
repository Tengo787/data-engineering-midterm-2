#!/bin/bash
docker build -t task7_image .
docker run --rm -v $(pwd):/app task7_image
