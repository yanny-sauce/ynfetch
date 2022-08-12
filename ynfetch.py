import platform
from uptime import uptime
import math
import getpass
import subprocess as sp
import os
import psutil

blsp = "              "
aski = []
user = getpass.getuser()+"@"+platform.node()
osys = ""
krnl = platform.platform()
modl = ""
proc = platform.processor()
memr = "" #METHOD DEPENDS ON THE PLATFORM
uptr = uptime()
uptm = int(uptr/60%60)
upth = int(uptr/60/60%24)
uptd = int(uptr/60/60/24)
uptr=str(uptm) + " minutes"
if upth != 0:
    uptr=str(upth)+ " hours, "+uptr
if uptd != 0:
    uptr=str(uptd)+ " days, " +uptr
pkgs = "" #METHOD DEPENDS ON THE PLATFORM AND DISTRIBUTION
finl = []

if "Linux" in krnl:
    modl = sp.getoutput("cat /sys/devices/virtual/dmi/id/product_version")
    krnl = krnl.split("-")[0]+"-"+krnl.split("-")[1]+"-"+krnl.split("-")[2]
    memd = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    memr = str(math.floor((int(memd['MemTotal'])-int(memd['MemFree'])-int(memd['Cached'])-int(memd['SReclaimable'])+int(memd['Shmem']))/1024)) + "M / " + str(math.floor(int(memd['MemTotal'])/1024))+"M"

    if "arch" in krnl:
        aski.append("      /\      ")
        aski.append("     /  \     ")
        aski.append("    /\   \    ")
        aski.append("   /      \   ")
        aski.append("  /   ,,   \  ")
        aski.append(" /   |  |  -\ ")
        aski.append("/_-''    ''-_\\")

        for cnt in range(0,7):
            aski[cnt]="\033[95m"+aski[cnt]+"\u001b[0m"

        osys = "Arch Linux"
        pkgs = sp.getoutput("pacman -Qq | wc -l")
        pkgs = str(pkgs) + " (pacman)"
    else:
        aski.append("      ___     ")
        aski.append("     (.. \    ")
        aski.append("     (<> |    ")
        aski.append("    //  \ \   ")
        aski.append("   ( |  | /|  ")
        aski.append("  _/\ __)/_)  ")
        aski.append("  \/-____\/   ")
        osys = "Linux (Unknown)"
        pkgs = "N/A"
elif "Windows" in krnl:
    memd=psutil.virtual_memory()
    memr=str(math.floor((int(memd[0])-int(memd[1]))/1024/1024)) + "M / "+str(math.floor(int(memd[0])/1024/1024))+"M"
    if "Windows-10" in krnl:
        aski.append("...... ......")
        aski.append(".    . .    .")
        aski.append("...... ......")
        aski.append("...... ......")
        aski.append(".    . .    .")
        aski.append("...... ......")
        aski.append("             ")
        osys = "Windows 10"
        pkgs = sp.getoutput('winget list | find /c /v ""') + " (winget)"
        modl = platform.uname().machine
        

finl.append(aski[0]+"   "+'\u001b[38;5;245m'+user+'\u001b[0m')
finl.append(aski[1]+"   OS:       "+osys)
finl.append(aski[2]+"   Host:     "+modl)
finl.append(aski[3]+"   Kernel:   "+krnl)
finl.append(aski[4]+"   Packages: "+pkgs)
finl.append(aski[5]+"   Memory:   "+memr)
finl.append(aski[6]+"   Uptime:   "+uptr)


for i in finl:
    print(i)

print()
