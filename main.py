device_1 = "SW-Nordvik-1"
model_1 = "WS-C3560G-48TS"
role_1 = "Switch, access"

device_2 = "R-Nordvik-1"
model_2 = "CISCO2951"
role_2 = "Router, lager 3"

device_3 = "Nordvik-trådlös"
model_3 = "tp-link-1"
role_3 = "wifi-spot"


print ("UTRUSTNINGSLISTA")
print ("-" * 52)

print (f"{device_1:<16}{model_1:<20}{role_1}")
print (f"{device_2:<16}{model_2:<20}{role_2}")
print (f"{device_3:<16}{model_3:<20}{role_3}")

print ("-" * 52)
print ("Antal enheter: 3")
# Har inget eget "rack" så kan inte göra steg 2.