import hashlib

pseudo = 'Clementine'
mdp = 'Clementine21!'

print(hashlib.sha256(pseudo.encode() + mdp.encode()).hexdigest())