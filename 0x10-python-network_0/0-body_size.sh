#!/bin/bash
# This is a Bash script that takes in a URL, sends a request to that URL, and displays the size (in bytes) of the body of the response, all using curl
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
