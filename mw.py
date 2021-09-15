import sys

mans = sys.argv[1].count("m")
Mdiag = "m " + "(" + str(mans) + ")"
if mans != 0:
    Mdiag += (" " + ("*" * mans))

womans = sys.argv[1].count("w")
Wdiag = "w " + "(" + str(womans) + ")"
if womans != 0:
    Wdiag += " " + ("*" * womans)

print(Mdiag + "\n" + Wdiag)

