#Mapquest Consumer Key
#pe3Md1LWEeotx4YqP17crn3HWZiIWyjO
#Error 404

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "pe3Md1LWEeotx4YqP17crn3HWZiIWyjO"

while True:
    units = input("Would you like to use miles or kilometers? Please enter either mi or km: ")
    if units == "quit" or units == "q":
        break
    if units != "mi" and units != "km":
        break
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        if units == "mi":
            print("Miles: " + str("{:.2f}".format(json_data["route"]["distance"])))
        if units == "km":    
            print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Tolls: " + str(json_data["route"]["hasTollRoad"]))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 403:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; API key error.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    elif json_status == 612:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; No routes available for location.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")