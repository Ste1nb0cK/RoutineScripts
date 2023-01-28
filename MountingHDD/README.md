# Mounting my HDD
This little script processes the list of disks given by `fdisk` and mounts a given disk using `mount`.

## Prerequisites
+
Python `3.9.2+`
+
`fdisk` and `mount`
+
`sudo` access to use `fdisk` and `mount` 

## How to use it 
Simply use

`sudo fdisk -l | python3 PathToScript/bigboy.py`

I have a dedicated alias for this and also one for unmounting.
