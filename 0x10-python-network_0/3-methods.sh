#!/bin/bash
# This is a Bash script that takes in a URL and displays all HTTP methods the server will accept, all using curl
curl -sI "$1" | grep Allow | cut -d " " -f2-
