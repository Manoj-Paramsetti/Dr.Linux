import os
import drlinux.listpkg as listpkg

if __name__ == "__main__":

    packages = os.listdir(".")
    print(packages)
    ignore = ["main.py", "LICENSE", "README.md", ".git", "drlinux"]
    for i in ignore:
        packages.remove(i)

    listpkg.main_logo()

    n = listpkg.showpkg(packages)

    listpkg.main_logo()

    listpkg.showfile(packages, n)
