#!/bin/bash
# This script send a deletes request to the file passed as an argument
curl -s -X DELETE "$1"
