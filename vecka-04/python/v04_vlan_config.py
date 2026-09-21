def vlan_config (number, name):
    rader = []
    rader.append (f"vlan {number}")
    rader.append (f" name {name}")
    return rader

for number in range (1, 41):
    vlan_namn = f"NAT{number:02d}"

    for rad in vlan_config (number, vlan_namn):
        print (rad)