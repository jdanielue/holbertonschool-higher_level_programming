#!/bin/bash
# displays the body of the response
curl -s -I "$1" | grep "Allow" | cut --complement -b1-7 --complement
