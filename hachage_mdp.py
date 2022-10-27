import hashlib

pseudos_mdp = {
    "Rebecca70" : "Armandblabla34!",
    "Aimée20" : "Hebertblublu20?",
    "Marielle90" : "Ribeiro38:)",
    "Hilaire100" : "Savary86;)",
    "GiGigigi" : "Armand38!",
    "Amy10" : "!!Heb2000",
    "Marie18" : "Rib380345!",
    "Hil100" : "Sava8634;)",
    "Amima20" : "Arm380!!!?",
    "Amira100" : "Hello2001__",
    "Maria180" : "Riban388!!",
    "Hihi100" : "Savane863:)"
}


mdp_hash = []

for key, value in pseudos_mdp.items():
    mdp_hash.append(hashlib.sha256(key.encode() + value.encode()).hexdigest())

print(mdp_hash)
print(pseudos_mdp.keys())

res = []

for pseudo, mdp in zip(pseudos_mdp.keys(), mdp_hash):
    res.append("("+pseudo+", "+mdp+")")

for item in res:
    print(item+',')