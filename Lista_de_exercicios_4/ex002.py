import os

if os.path.exists("atividaderemove.txt"):
    os.remove("atividaderemove.txt")
    print("arquivo existe e foi removido")
    
    
else:
    print("arquivo não existe")
