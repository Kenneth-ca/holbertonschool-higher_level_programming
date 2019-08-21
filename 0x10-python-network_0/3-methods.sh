#!/bin/bash
# Takes in a URL and displays all HTTP methods
curl -si -X OPTIONS $1 | grep Allow | cut -d" " -f 2-5
