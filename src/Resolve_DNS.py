
import socket 

def Resolve_DNS():

# Loop to get URL and resolve its IP address. 
    while True:
        try:
            url = input("Enter Target URL: ")
            data = socket.gethostbyname(url)
            ip = repr(data)
            print("\n The IP Address found is: "+ ip)
            return ip
        except:
            print("url was incorrectly entered, try again.")
        else: 
            break

if __name__ == "__main__":
    Resolve_DNS