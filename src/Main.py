
from Resolve_DNS import *
from Find_IP_location import *

def main():
    print("Start of BBRECON....\n")
    IP = Resolve_DNS()
    formatted_IP = IP.translate({ord("'"): None})
    IP_Location = Get_Location(formatted_IP)

if __name__ == "__main__":
    main()