import subprocess
import sys
import os
#info to identify the disk
aux = "Disk model: "
disk_model = "TOSHIBA MQ04ABF1"
target = aux + disk_model
#Mounting info
mount_direction = '/SanJuanWolf'
#Check that the mounting directory exists, create it in case it doesn't
if not os.path.exists(mount_direction):
    print("The mounting direction does not exists, creating it.")
    subprocess.run(["sudo", "mkdir", mount_direction], shell=False)
    print("Mounting direction created at {}".format(mount_direction))
else:
    print("The mounting direction exists.")
#identification of the device
print("Initiating Identification.")
input = sys.stdin.read()
cut_index = input.find(target)
cutted_input = input[cut_index::]
splitted = cutted_input.splitlines()
candidate_line = splitted[8]
if (candidate_line.endswith('Linux filesystem')): #check that the line is valid
    device = candidate_line.split()[0]
#mount the disk
print("Mounting")
subprocess.run(["sudo", "mount", device, mount_direction], shell=False)
print("Mounted at {}".format(mount_direction))
print("------------------------------Ya no estoy chikito------------------------------")
