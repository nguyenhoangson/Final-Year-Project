#!/bin/bash

#simple script for resizing images in all class directories
#also reformats everything from whatever to png

# run the script as ./resize_images.sh folder_1 folder_2 ... folder_n

for folder in $@; do 

    # Check if there are any .jpg files
    if [ `ls $folder/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
	echo "Resizing .jpg images in $folder..."
	for file in $folder/*/*.jpg; do
	    convert "$file" -resize 28x28\! "${file%.*}.png"
	    file "$file" #uncomment for testing
	    rm "$file"
	done
	echo "Done resizing .jpg in $folder"
    fi

    # Check if there are any .png files
    if [ `ls $folder/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
	echo "Resizing .png images in $folder..."
	for file in $folder/*/*.png; do
	    convert "$file" -resize 28x28\! "${file%.*}.png"
	    file "$file" #uncomment for testing
	done
	echo "Done resizing .png in $folder"
    fi

    # Check if there are any .jpeg files
    if [ `ls $folder/*/*.jpeg 2> /dev/null | wc -l ` -gt 0 ]; then
	echo "Resizing .jpeg images in $folder..."
	for file in $folder/*/*.jpeg; do
	    convert "$file" -resize 28x28\! "${file%.*}.png"
	    file "$file" #uncomment for testing
	    rm "$file"
	done
	echo "Done resizing .jpeg in $folder"
    fi

done 
