import json

auto = {
    "marca":"Toyota",
    "modello":"Supra mk4",
    "anno_produzione":1993,
    "potenza_kW":243,
    
}

print(type(auto))
print(auto)

print(json.dumps(auto))


f = open("myJSON.json","w")
f.write(json.dumps(auto))
f.close()