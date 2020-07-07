import sys
import os

def Restart_re():
    if(os.path.exists("/run/restart-required")):
        return True

    return False

def main():

    if(Restart_re()):
        print("Restart required")
        sys.exit(1)

    print("Restart not required")
    sys.exit(0)

main()
