import sys
import os

def alko(typ):
        if typ=="mickiewicz":
                print("Walisz z matim")
        elif typ=="zubrowka":
                print("konczymy balety")
        elif typ=="grey goose":
                print("Walisz z mr polsak")
        elif typ=="AMARENE":
                print("spierdalaj")
                exit()
        elif typ == "General":
                import webbrowser
                webbrowser.open("https://pornhub.com", new=2)
        elif typ == "JESTE ABSYNENTE":
                print("mizg")

while True:
        x=input("WYCHLEJESZ WODECZKE? [Tak/Nie]: ")

        if x=="Nie":   
                print()
        elif x=="Tak":
                print("Dostepene: ")
                print("1. mickiewicz")
                print("2. zubrowka")
                print("3. grey goose")
                print("4. AMARENE")
                print("5. General")
                print("6. JESTE ABSTYNENTE")
                alko(input("WYYBPITEQRAASDJ: "))
        elif x=="NADCZLOWIEK":
                print("BROKE ASS NIGGA")
        else:
                print("OSZ TY CHUJU")
        print("No wez jeszcze co ty pizda?\n\n")
      
