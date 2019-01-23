from SheetReader import SheetReader
from CardGenerator import CardGenerator

def main():
    sr = SheetReader()
    cg = CardGenerator()

    values = sr.readSheet()
    for row in values:
        cg.addNote(row[0], row[1])

if __name__ == '__main__':
    main()