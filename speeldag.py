Ticket = float (7.45)
Aantalvriend = int(input('Hoeveel vrienden komen mee ?'))
VRSpelen = int(input('Hoelang op de VR ?'))
VIPMinuut = float (0.37)
Totalevrienden = Aantalvriend * Ticket
TotaleVRTime = VIPMinuut * VRSpelen
print (Totalevrienden)
print ("Totaal prijs is:",int((Totalevrienden + TotaleVRTime)*100), "cent")

