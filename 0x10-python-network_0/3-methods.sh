!/bin/bash
# displays the body of the response
curl -s -I "$1" | grep "Allow" | cut --complement -d':'  -f1
