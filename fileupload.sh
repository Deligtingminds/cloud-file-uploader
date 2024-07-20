#!/bin/bash

FILEPATH=/Users/yinkabakare/downloads


read -p " Enter File Name " FILENAME

FULLPATH="$FILEPATH/$FILENAME"

  if [ -f "$FULLPATH" ]; then
    echo "File provided: $FILENAME"
  else
    echo "Error: File does not exist in the downloads folder."
    exit 1
fi


BUCKET_NAME="fileupload5678483"


aws s3 cp "$FULLPATH" "s3://$BUCKET_NAME/$FILENAME"

FILESIZE=$(stat -f%z "$FULLPATH")

pv -s "$FILESIZE" "$FULLPATH" | aws s3 cp - "s3://$BUCKET_NAME/$FILENAME"
