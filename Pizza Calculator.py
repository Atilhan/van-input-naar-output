#Atilhan Kara Pizza Calculator 99024233

#Deze variables geven de prijzen aan van de pizza's (van klein naar groot)
PizzaSmall = float(8.50)
PizzaMedium = float(12.50)
PizzaLarge = float(16.50)
#Deze datatypes geven een imput (prompt) aan die je de vraagt stelt hoeveel pizza's u wilt bestellen
PizzaSmallAantal = int(input('Kies de aantal Small Pizzas dat u wilt: '))
PizzaMediumAantal = int(input('Kies de aantal Small Pizzas dat u wilt: '))
PizzaLargeAantal = int(input('Kies de aantal Small Pizzas dat u wilt: '))
#De totaal prijs rekent de kleine tot de grote pizza's op
TotaalPrijs = ((PizzaSmall * PizzaSmallAantal) + (PizzaMedium * PizzaMediumAantal) + (PizzaLarge * PizzaLargeAantal))
#De aantal pizza's dat u gekozen heeft word uitberekend
print ('De pizza die u heeft gekozen ' + str(PizzaSmallAantal) , 'Small Pizza,' , str(PizzaMediumAantal), 'Medium Pizza,', str(PizzaLargeAantal) , "Large Pizza's besteld. Uw totaal prijs is:" ,TotaalPrijs, '€')

