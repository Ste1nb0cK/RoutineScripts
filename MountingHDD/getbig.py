import os
import sys

#info to identify the disk
aux = "Disk model: "
disk_model = "TOSHIBA MQ04ABF1"
target = aux + disk_model
#Mounting info
mount_direction = '/SanJuanWolf'
#Check that the mounting directory exists, create it in case it doesn't
if not os.path.exists(mount_direction):
    os.system('mkdir {}'.format(mount_direction))
else:
    print("The mounting direction exists. Proceeding to mounting.")
#identification of the device
input = sys.stdin.read()
cut_index = input.find(target)
cutted_input = input[cut_index::]
splitted = cutted_input.splitlines()
candidate_line = splitted[8]
if (candidate_line.endswith('Linux filesystem')): #check that the line is valid
    device = candidate_line.split()[0]
#mount the disk
os.system('sudo mount {} {}'.format(device, mount_direction))
print("Ya no estoy chikito")
