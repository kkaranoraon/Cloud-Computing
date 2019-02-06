#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('dname')
os_ram=web.getvalue('dram')
os_cpu=web.getvalue('dcpu')
os_hdd=web.getvalue('disk')

#  a fresh copy 
commands.getoutput('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')


print os.system('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2 				      --graphics=vnc,listen=192.168.10.129,port=6666,password=karan --import --noautoconsole')

print os.system('sudo websockify --web=/usr/share/novnc 7056 192.168.10.129:6668')
print os.system('sudo qr 192.168.10.129:7056 > /var/www/html/iaas.png')
