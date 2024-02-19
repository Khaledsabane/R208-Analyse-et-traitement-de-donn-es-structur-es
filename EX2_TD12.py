import sys
def main():
    if len(sys.argv)>=2:
        filename=sys.argv[1]
        fichier=open(filename, 'r')
        i=0
        for p in fichier:
            p=p.rstrip("\n\r")
            print(f"{i} .\t {p}")
            i+=1
if __name__=="__main__":
         sys.exit((main()))
