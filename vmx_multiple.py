import wget
import tarfile
import os
from shutil import copy

fpc_count = int(input('Enter the number of fpc, maximum possible value 12:'))
mpc = input('Select the size of RAM for the MPC module, the possible values are 2, 4, or 10 :')
mpc = 'metadata-usb-service-pic-' + mpc +'g.img'

URL = "http://dsv.yamalzdrav.ru/Juniper/vMX/vmx-bundle-22.4R1-S1.1.tgz"

response = wget.download(URL, "/tmp/vmx-bundle-22.4R1-S1.1.tgz")

print('Extracting the archive\n\n')

vmx = '/tmp/vmx-bundle-22.4R1-S1.1.tgz'
tar = tarfile.open(vmx, "r:gz")
tar.extractall('/tmp/')
tar.close()

img_dir = '/tmp/vmx/images/'
eve_dir = '/opt/unetlab/addons/qemu/'

for i in range(fpc_count):
   if i == 0:
      image = img_dir + mpc
   else:
      image = img_dir + 'metadata-usb-fpc' + str(i) + '.img'
   fpc_dir = eve_dir + 'vmxvfp-22.4R1-S1.1-VFP-fpc' + str(i) + '/'
   try:
      os.mkdir(fpc_dir)
   except:
      print('directory already exists')
      continue

   src_path = img_dir + 'vFPC-20221102.img'
   destination_path = fpc_dir + 'virtioa.qcow2'
   copy(src_path, destination_path)

   src_path = image
   destination_path = fpc_dir + 'virtiob.qcow2'
   copy(src_path, destination_path)
   print('Copying fpc' + str(i) + ' is complete\n\n')


re0_dir = eve_dir + 'vmxvcp-22.4R1-S1.1-VCP-re0/'
try:
   os.mkdir(re0_dir)
except:
   print('directory already exists\n')

re1_dir = eve_dir + 'vmxvcp-22.4R1-S1.1-VCP-re1/'
try:
   os.mkdir(re1_dir)
except:
   print('directory already exists\n')

src_path = img_dir + 'junos-vmx-x86-64-22.4R1-S1.1.qcow2'
destination_path = re0_dir + 'virtioa.qcow2'
copy(src_path, destination_path)

src_path = img_dir + 'vmxhdd.img'
destination_path = re0_dir + 'virtiob.qcow2'
copy(src_path, destination_path)

src_path = img_dir + 'metadata-usb-re0.img'
destination_path = re0_dir + 'virtioc.qcow2'
copy(src_path, destination_path)
print('Copying re0 is complete\n\n')


src_path = img_dir + 'junos-vmx-x86-64-22.4R1-S1.1.qcow2'
destination_path = re1_dir + 'virtioa.qcow2'
copy(src_path, destination_path)

src_path = img_dir + 'vmxhdd.img'
destination_path = re1_dir + 'virtiob.qcow2'
copy(src_path, destination_path)

src_path = img_dir + 'metadata-usb-re1.img'
destination_path = re1_dir + 'virtioc.qcow2'
copy(src_path, destination_path)
print('Copying re1 is complete\n\n')
