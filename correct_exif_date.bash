#this script gets the file modified date and if older than the exif date (or the exif date does not exist)
#it adds an exif date to the file. it then changes the modified date back to the original one.
#maybe it should also change the modified date if the exif date is older.


#!/bin/bash

# specify folder path
folder_path="/home/user/pics"

# find all image files in folder and subfolders
find "$folder_path" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0 | while IFS= read -r -d '' file; do
  # get file modified date
  modify_date=$(stat -c %y "$file")

  # get exif date using exiftool
  exif_date=$(exiftool -CreateDate "$file" | awk '{print $4}')

  # check if exif date is newer or doesn't exist
  if [[ -z "$exif_date" || "$exif_date" > "$modify_date" ]]; then
    # change/create exif date tag with older date
    exiftool -overwrite_original -CreateDate="$modify_date" "$file"
    touch -c -d "$modify_date" "$file"
  fi


done
