#!/bin/bash
# Takes in a URL and displays all HTTP methods
curl -si -X OPTIONS --head 0.0.0.0:5000/route_4 | grep Allow | cut -d" " -f 2-5
