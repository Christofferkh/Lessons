vendors = {
    "a4:c3:f0": "Intel",
    "3c:d9:2b": "Hewlett-Packard",
    "00:1a:a1": "Cisco Systems",
#egen
    "e0:55:3d": "Cisco Meraki",
    "90:4C:C5": "Apple, Inc.",
    "f8:9e:28": "Cisco Meraki",
}

addresses = [
    "a4:c3:f0:11:3a:b7",
    "3c:d9:2b:d2:11:88",
    "8c:85:90:44:12:0e",
#egen
    "e0:55:3d:e1:27:c0",
    "90:4C:C5:CD:9E:73",
    "f8:9e:28:74:0c:09",
]

for address in addresses:
    prefix = address [0:8]
    
    if prefix in vendors:
        name = vendors[prefix]
    else:
        name = "okänd tillverkare"
    
    print(f"{address}  ->  {name}") 