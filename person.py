AantalCroissants = 17
PrijsCroissant = 0.39
AantalStokbrood = 2
PrijsStokbrood = 2.78
KortingBon = 0.50
AantalKortingBon = 3
PrijsFeestLunch = 10.69
Uitkomst = '(AantalCroissant * PrijsPerCroissant)'

print((AantalCroissants * PrijsCroissant) + (AantalStokbrood * PrijsStokbrood) - (AantalKortingBon * KortingBon))
print('De feestlunch kost je bij de bakker '+ str(PrijsFeestLunch) +' voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')

print('Bedrag berekenen')
PrijsPerCroissant = int(input('Wat zijn de kosten van de croissants?'))
AantalCroissant = int(input('Hoeveel crossaints wil je?'))
Uitkomst = (AantalCroissant * PrijsPerCroissant)
print(str(Uitkomst) +' cent')