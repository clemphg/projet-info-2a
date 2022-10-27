import hashlib

pseudo = "Aimee20"
mdp = "Hebertblublu20?"

mdp_hache = hashlib.sha256(pseudo.encode() + mdp.encode()).hexdigest()

print(mdp_hache)