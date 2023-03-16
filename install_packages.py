import pip
import argparse

#################### CONFIG ####################

core_packages = ["mouse", "keyboard", "requests"]
extra_packages = ["bleak", "hue-py", "phue",
                  "cv2", "numpy"]

################################################

parser = argparse.ArgumentParser(description='Python module installer v1.0')
parser.add_argument('--scope',
                    help = "core | all")
args = parser.parse_args()

errors = []

def pip_install(package):
    try:
        pip.main(["install", package])
        print(colored("[OK] Successfully installed "+package, "green"))
    except Exception as error:
        print(colored("[Error] Could not install "+package, "red"))
        errors.append("[Error] Could not install "+package)
        errors.append("["+package+" >_] "+error)

# install package for colored terminal output
try: 
    from termcolor import colored
    # https://pypi.org/project/termcolor/
except ModuleNotFoundError:
    pip_install("termcolor")
    from termcolor import colored

print(colored("> Installing core packages\n", "dark_grey"))
for package in core_packages:
    pip_install(package)
    
if args.scope == "all":
    print(colored("> Installing extra packages\n", "dark_grey"))
    for package in extra_packages:
        pip_install(package)
        
print(colored("Complete.", "dark_grey"))

if len(errors) > 0:
    print("The script encountered the following errors whilst attempting installs.")
    for error in errors:
        print(colored(error, "red"))


