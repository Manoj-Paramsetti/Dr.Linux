import os
import drlinux.listpkg as listpkg

if __name__ == "__main__":
    file = listpkg.askWhat()
    packages = os.listdir(file)
    print(packages)
    n = listpkg.showpkg(packages)
    listpkg.showfile(file, packages, n)
