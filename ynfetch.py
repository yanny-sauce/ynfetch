import platform
import math
import getpass
import subprocess as sp
import os
try:
    from uptime import uptime
except ModuleNotFoundError:
    print("Module uptime missing, would you like to install it? Y/N")
    ans=input()
    if ans=="Y":
        os.system("pip install uptime")
        exit()
try:
    import psutil
except ModuleNotFoundError:
    print("Module psutil missing, would you like to install it? Y/N")
    ans=input()
    if ans=="Y":
        os.system("pip install psutil")
        exit()

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
    osys = sp.getoutput("cat /etc/os-release")
    for i in osys.split("\n"):
        if i.split('=')[0]=="NAME":
            osys=i.split('=')[1].split('"')[1]

    modl = sp.getoutput("cat /sys/devices/virtual/dmi/id/product_version")
    krnl = krnl.split("-")[0]+"-"+krnl.split("-")[1]+"-"+krnl.split("-")[2]
    memd = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    memr = str(math.floor((int(memd['MemTotal'])-int(memd['MemFree'])-int(memd['Cached'])-int(memd['SReclaimable'])+int(memd['Shmem']))/1024)) + "M / " + str(math.floor(int(memd['MemTotal'])/1024))+"M"

    if osys=="Arch Linux":
        aski.append("      /\      ")
        aski.append("     /  \     ")
        aski.append("    /\   \    ")
        aski.append("   /      \   ")
        aski.append("  /   ,,   \  ")
        aski.append(" /   |  |  -\ ")
        aski.append("/_-''    ''-_\\")
        pkgs = sp.getoutput("pacman -Qq | wc -l")
        pkgs = pkgs + " (pacman)"
    elif osys=="Artix Linux":
        aski.append("        /\      ")
        aski.append("       /  \     ")
        aski.append("      /`'.,\    ")
        aski.append("     /     ',   ")
        aski.append("    /      ,`\  ")
        aski.append("   /   ,.'`.  \ ")
        aski.append("  /.,'`     `'.\\")
        pkgs = sp.getoutput("pacman -Qq | wc -l")
        pkgs = pkgs + " (pacman)"
    elif osys=="Ubuntu":
        aski.append("         _   ")
        aski.append("     ---(_)  ")
        aski.append(" _/  ---  \  ")
        aski.append("(_) |   |    ")
        aski.append("  \  --- _/  ")
        aski.append("     ---(_)  ")
        aski.append("             ")
        pkgs = sp.getoutput("dpkg -l | wc -l")
        pkgs = pkgs + " (dpkg)"
    elif osys=="Linux Mint":
        aski.append(" ___________  ")
        aski.append("|_          \ ")
        aski.append("  | | _____ | ")
        aski.append("  | | | | | | ")
        aski.append("  | | | | | | ")
        aski.append("  | \_____/ | ")
        aski.append("  \_________/ ")
        pkgs = sp.getoutput("dpkg -l | wc -l")
        pkgs = pkgs + " (dpkg)"
    elif osys=="Fedora Linux":
        aski.append("       ^^~^~^:")
        aski.append("      ^^~. :~!")
        aski.append("    . ^:~   ::")
        aski.append(".:^^^~^.^^~.  ")
        aski.append("~^:.  ^:~     ")
        aski.append("~^:  .~^^     ")
        aski.append(".^~~^~^^      ")
        pkgs = sp.getoutput("dnf list installed | wc -l")
        pkgs = pkgs + " (dnf)"
    elif osys=="Manjaro Linux":
        aski.append("||||||||| ||||")
        aski.append("||||||||| ||||")
        aski.append("||||      ||||")
        aski.append("|||| |||| ||||")
        aski.append("|||| |||| ||||")
        aski.append("|||| |||| ||||")
        aski.append("|||| |||| ||||")
        pkgs = sp.getoutput("pacman -Qq | wc -l")
        pkgs = pkgs + " (pacman)"
    else:
        aski.append("      ___     ")
        aski.append("     (.. \    ")
        aski.append("     (<> |    ")
        aski.append("    //  \ \   ")
        aski.append("   ( |  | /|  ")
        aski.append("  _/\ __)/_)  ")
        aski.append("  \/-____\/   ")
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
        
for cnt in range(0,7):
    aski[cnt]="\033[95m"+aski[cnt]+"\u001b[0m"

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
