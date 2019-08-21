#!/bin/bash
# Header variable to the URL email, subject
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
