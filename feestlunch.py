Crossant  = float(0.39) 
HoeveelCrossant = int(input('Hoeveel crossant wil je ? '))
Stokbrood = float(2.78)
HoeveelStokbrood = int(input('Hoeveel stokbrood wil je ? '))
Kortingsbon = float (1.50)
KortingsbonPrijs = float (0.50)
KortingsHoeveel = float(input('Hoeveel kortings bonnen heb je? '))

print (int(((HoeveelCrossant * Crossant) + (HoeveelStokbrood * Stokbrood) - (KortingsbonPrijs * KortingsHoeveel))*100),"cent")
