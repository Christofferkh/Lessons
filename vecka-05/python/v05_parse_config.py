filnamn = r"C:\Users\krill\Documents\Lessons\vecka-05\configs\r1-show-run.txt"

routes = []
interfaces = []

with open(filnamn) as f:
    for rad in f:
        rad = rad.strip()
        
        if rad.startswith("ip route "):
            routes.append(rad)
        
        elif rad.startswith("interface "):
            interfaces.append(rad)
            
print(f"Hittade {len(routes)} statiska rutter:")
for rad in routes:
    print(f"  {rad}")
    
print ()

print(f"Hittade {len(interfaces)} interfaces:")
for rad in interfaces:
    print(f"  {rad}")