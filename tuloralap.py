from fuggvenyeim.rutinok import honap_atalakito, napok_validalas, szakok_validalasa



honap = str.capitalize(input("Kérem a hónapot:"))
while honap_atalakito(honap) == False:
    print("Kérem adjon meg létező hónap nevet. pl. 01, Január, stb:")
    honap = str.capitalize(input("Kérem a hónapot:"))

nap = str(input("Kérem a napot:"))
while napok_validalas(nap) == False:
    print("Kérem adjon meg 1 -31 közötti számot, figyeljen, hogy az aktuális hónap tartalmazzon enny napot!")
    nap = str(input("Kérem a napot:"))

szak = input("Melyik szak (két karakterrel, pl. B1 vagy H5 stb.):")
while szakok_validalasa(szak) == False:
    print("Kérem dajon meg valós szakot!")
    szak = input("Melyik szak (két karakterrel, pl. B1 vagy H5 stb.):")

honap = honap_atalakito(honap)
nap = napok_validalas(nap)
szak = szakok_validalasa(szak)

print(honap, nap, szak)

