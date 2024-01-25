#!/usr/bin/env bash

source=$(who | awk '{print $1}')

echo $source

#echo "the source is $source"

echo "enter Dest username"

read user

echo starting transfer....

scp -r /home/$source/Desktop/Captures $user@192.168.1.11:/home/$user/Desktop
if [ $? -ne 0 ]; then
    echo "Error: scp command for Captures directory failed."
    exit 1
fi

echo starting transfer for panorama results

scp -r /home/$source/Desktop/panorama_results $user@192.168.1.11:/home/$user/Desktop
if [ $? -ne 0 ]; then
    echo "Error: scp command for panorama_results directory failed."
    exit 1
fi

echo transfer completed..

exit    