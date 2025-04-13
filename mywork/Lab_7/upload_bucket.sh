#!/bin/bash

#assign args
FILE=$1
BUCKET=$2
EXPIRATION=$3

#valid each of the inputs
if [ $# -ne 3 ]; then
	echo "Usage: $0 <file> <bucket> <expiration>"
	exit 1
fi

#upload file to s3 bucket
aws s3 cp "$FILE" "s3://$BUCKET/"

#output expiration info and confirm
echo "Presigned URL that expires in $EXPIRATION seconds:"
aws s3 presign "s3://$BUCKET/$(basename "$FILE")" --expires-in $EXPIRATION
