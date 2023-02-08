#!/bin/bash

find . -type f -exec perl -pi -e 's!.!.!g;' *.html {} +