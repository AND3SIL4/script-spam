import os
import subprocess
import sys

def create_virtualenv(env_name):
    subprocess.check_call([sys.executable, "-m", "virtualenv", env_name])
    activate_script = os.path.join(env_name, "Scripts", "activate") if os.name == "nt" else os.path.join(env_name, "bin", "activate")
    return activate_script

def install_requirements(env_name, requirements_file):
    if os.name == "nt":
        pip_path = os.path.join(env_name, "Scripts", "pip.exe")
    else:
        pip_path = os.path.join(env_name, "bin", "pip")

    subprocess.check_call([pip_path, "install", "-r", requirements_file])

def main():
    env_name = "virt"
    requirements_file = "requirements.txt"

    create_virtualenv(env_name)
    install_requirements(env_name, requirements_file)


if __name__ == "__main__":
    main()
