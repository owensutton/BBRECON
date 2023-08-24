
#  Given an IP address find the geographical location of the address. 

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance


def Get_Location(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


if __name__ == "__main__":
    Get_Location()