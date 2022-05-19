#!/bin/bash
# This is a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX "$1" GET -H "X-HolbertonSchool-User-Id: 98"
