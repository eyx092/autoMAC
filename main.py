import socket
import random
import time
import sys
import subprocess
from termcolor import cprint

REMOTE_SERVER = "google.com"


def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except socket.gaierror:
        pass
    return False


def generate_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


print("autoMAC v0.0.1")


if sys.platform != "darwin":
    cprint("This program is only compatible with MacOS.", "red")
    cprint("Closing...", "blue")
    sys.exit(0)


while True:
    print("1. Start (S)")
    print("2. Exit (E)")
    option = input()
    if option.lower() == "s" or option == "1" or option.lower() == "start":
        cprint("Starting...", "blue")
        print("Press Control-C to quit.")
        while True:
            try:
                time.sleep(1)
                cprint("Checking...", "blue")
                if is_connected(REMOTE_SERVER) is False:
                    cprint("No connection.", "red")
                    cprint("Attempting to change MAC Address...", "blue")
                    try:
                        mac_address = generate_mac()
                        subprocess.run(["sudo", "ifconfig", "en0", "ether", mac_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        cprint(f"Success! MAC Address set to: {mac_address}", "green")
                    except FileNotFoundError:
                        cprint("Change failed.", "red")
                else:
                    cprint("Connection is good.", "green")
            except KeyboardInterrupt:
                break
    if option.lower() == "e" or option == "2" or option.lower() == "exit":
        cprint("Exiting...", "blue")
        sys.exit(0)
