#
#   Name: BBRECON
#   Created By: Owen Sutton
#   Description: Bug Bounty Recon tool. 
#
#   Version 1.01
#   Latest Issue: Owen-resolve-dns-to-ip-address
#

from Resolve_DNS import *

def main():
    print("Start of BBRECON....\n")
    Resolve_DNS()

if __name__ == "__main__":
    main()