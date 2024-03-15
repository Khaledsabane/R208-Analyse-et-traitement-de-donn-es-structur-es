with open("myfile.txt","r") as fichier:
    l =fichier.readlines()

    i=0
    for ligne in l:
       ligne = ligne.strip("\r\n") # A quoi sert rstrip ???

       if ligne.strip():
          f = open(f"f{i}.txt", "w")
          f.write(ligne)
          i+=1
          print(ligne,i)
