#hier wordt alles import (van rich)
import rich
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table



def toon_contacten(l):
    #laat zien welke contacten je hebt
    table = Table(title="contacten")

    table.add_column("naam", style="magenta")
    table.add_column("telefoonnummer", justify="right", style="green")

    for key, value in l.items():
        table.add_row(key, value)

    console = Console()
    console.print(table)

def aantal_contacten(l):
    #laat zien hoeveel contacten je hebt
    aantal = len(l)
    print("je hebt", aantal, "contacten")

def toevoegen(l):
    naam = input("naam? ")
    nummer = input("telefoonnummer? ")
    l[naam] = nummer
    
    table = Table(title="contacten")

    table.add_column("naam", style="magenta")
    table.add_column("telefoonnummer", justify="right", style="green")

    for key, value in l.items():
        table.add_row(key, value)

    console = Console()
    console.print(table)

    return l

def aanpassen(l):
    #pas een contact die al in je lijst staat aan
    table = Table(title="contacten")

    table.add_column("naam", style="magenta")
    table.add_column("telefoonnummer", justify="right", style="green")

    for key, value in l.items():
        table.add_row(key, value)

    console = Console()
    console.print(table)
    welke = Prompt.ask("welke? ", choices=l.keys())
    vervang = Prompt.ask("nieuwe naam? ", default=welke)
    vervang2 = input("nummer? ")
    if welke in l:
        del l[welke]
        l[vervang] = vervang2

        table = Table(title="contacten")

        table.add_column("naam", style="magenta")
        table.add_column("telefoonnummer", justify="right", style="green")

        for key, value in l.items():
            table.add_row(key, value)

        console = Console()
        console.print(table)

        return l
    else:
        print("dit nummer bestaat helaas niet")

def verwijderen(l):
    #verwijder een contact uit je lijst
    table = Table(title="contacten")

    table.add_column("naam", style="magenta")
    table.add_column("telefoonnummer", justify="right", style="green")

    for key, value in l.items():
        table.add_row(key, value)

    console = Console()
    console.print(table)
    
    verwijderen = Prompt.ask( "welke? ", choices=l.keys())
    if verwijderen in l:
        del l[verwijderen]
        
        table = Table(title="contacten")

        table.add_column("naam", style="magenta")
        table.add_column("telefoonnummer", justify="right", style="green")

        for key, value in l.items():
            table.add_row(key, value)

        console = Console()
        console.print(table)
        print(verwijderen + " is verwijderd")

        return l
    else:
        print("dit nummer bestaat helaas niet")

def main():
    #hier wordt het hele programma gestart en wordt gezegt welke def uitgevoert moet worden
    contacten = {"buurman": "1123043", "mam": "1123432", "papa": "1123850", "daddy": "1123759", "hans": "1125738"}
    
    while (stoppen := Prompt.ask("wil je stoppen? ", choices=["ja", "nee"], default="nee") != "ja"):
        
        table = Table(title="wat te doen?")

        table.add_column("naam", style="magenta")
        table.add_column("telefoonnummer", justify="right", style="green")

        table.add_row("1.", "toon contacten")
        table.add_row("2.", "voeg contact toe")
        table.add_row("3.", "pas contact aan")
        table.add_row("4.", "verwijder contact")

        console = Console()
        console.print(table)

        keuze = Prompt.ask("welke wil je doen? ", choices=["1", "2", "3", "4"], default="1")

        if keuze == "1":
            toon_contacten(contacten)
            aantal_contacten(contacten)
        elif keuze == "2":
            contacten = toevoegen(contacten)
        elif keuze == "3":
            aanpassen(contacten)
        elif keuze == "4":
            verwijderen(contacten)
        else:
            print("sorry, maar dat begrijp ik niet")


#eerlijk gezegt heb ik geen idee wat deze doet, maar het programma werkt niet
#zonder
if __name__ == "__main__":
    main()
