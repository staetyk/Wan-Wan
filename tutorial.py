from time import sleep

watch = ""
while watch not in ["lon", "ala"]:
    print("\u001b[2J\u001b[H\u001b[m", end = "")
    watch = input("sina wile ala wile lukin e open sona?\n\u001b[2;3m(lon/ala)\u001b[m\n").lower().replace(" ", "")
print("\u001b[2J\u001b[H\u001b[m", end = "")
watch = watch == "lon"

if watch:
    txt = [
        "sina jo e nimi tu la open.",
        "o pana e nimi tu tan wan e nimi.",
        "o pana e '?' la sina wile lukin e pali pini sina.",
        #"o pana e '!' la sina wile lukin e sona lili.",
        "nimi li nimi pu la linja lon anpa nimi.\nnimi lon insa kulupu la nimi li kule.",
        "kulupu loje li nimi soweli.\nkulupu jelo li nimi sijelo.\nkulupu laso loje li nimi kule.\nkulupu laso jelo li nimi nasin.\nkulupu laso li nimi lipu.",
        "o alasa alasa pini e nimi ale li musi a!"
    ]
    for x in txt:
        lines = x.split("\n")
        for i in range(len(lines)):
            print(lines[i])
            if i + 1 < len(lines):
                sleep(1)
        input("\u001b[8m")
        print("\u001b[2J\u001b[H\u001b[m", end = "")