import os


def main_logo():
    ### Colors
    normal = "\033[0;0;0m"
    underlined_text = "\033[2;37;40m"
    green = "\033[1;32;40m"

    os.system("clear")
    print(
        '''
	 M""""""'YMM             M""MMMMMMMM oo                            
	 M  mmmm. `M             M  MMMMMMMM                               
	 M  MMMMM  M 88d888b.    M  MMMMMMMM dP 88d888b. dP    dP dP.  .dP 
	 M  MMMMM  M 88'  `88    M  MMMMMMMM 88 88'  `88 88    88  `8bd8'  
	 M  MMMM' .M 88       dP M  MMMMMMMM 88 88    88 88.  .88  .d88b.  
	 M       .MM dP       88 M         M dP dP    dP `88888P' dP'  `dP 
	 MMMMMMMMMMM             MMMMMMMMMMM                               
	'''
    )

    try:
        os.system("./drlinux/blink")
    except:
        os.system("chmod +x drlinux/blink")
        os.system("chmod +x drlinux/offblink")

    print(green, "                  Created by Manoj Paramsetti                     ")
    print(normal)


### Colors
normal = "\033[0;0;0m"
underlined_text = "\033[2;37;40m"
green = "\033[1;32;40m"

def askWhat():
    main_logo()
    print('1. Installation')
    print('2. Error Fix')

    n = int(input(green + "\nEnter your option number" + normal + "\n>>>")) - 1

    if(n ==0):
        return "installation"
    else:
        return "treatment"

def showpkg(packages):
    main_logo()

    length = len(packages)
    os.system("./drlinux/offblink")

    for i in range(0, length):
        print(f"{i+1}. {packages[i]}")
    n = int(input(green + "\nEnter your option number" + normal + "\n>>>")) - 1
    return n


def showfile(folder, packages, n):
    main_logo()

    files = os.listdir(folder+'/'+ packages[n])
    length = len(files)

    for i in range(0, length):
        print(f"{i+1}. {files[i].capitalize().replace('_', ' ').replace('.sh','')}")

    file = int(input(green + "\nEnter your option number" + normal + "\n>>>"))

    os.system("chmod +x " + folder + "/" + packages[n] + "/" + files[file - 1])
    os.system("./" + folder + "/" + packages[n] + "/" + files[file - 1])
