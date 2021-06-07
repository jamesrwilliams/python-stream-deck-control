import os
import subprocess

def start_docker():
    s = subprocess.check_output('docker ps', shell=True)

    print(s)

    if s != 0:
        run = os.system('open /Applications/Docker.app')
    else:
        print('Docker daemon is running')


if __name__ == "__main__":
    start_docker()


