from subprocess import check_output
from json import loads
import sys

if len(sys.argv) != 1:
	result = loads(check_output(f"curl --silent https://freegeoip.app/json/{sys.argv[1]}", shell=True).decode("utf-8"))
else:
	result = str(check_output("curl --silent ifconfig.me", shell=True)).split('\'')
	result = loads(check_output(f"curl --silent https://freegeoip.app/json/{result[1]}", shell=True).decode("utf-8"))

print("IP: " + result["ip"])
print("Country: " + result["country_name"])
print("Region: " + result["region_name"])
print("City: " + result["city"])
print("Latitude: " + str(result["latitude"]))
print("Longitude: " + str(result["longitude"]))