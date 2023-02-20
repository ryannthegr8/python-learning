temperature = input("Enter today's temperature: ")

if int(temperature) > 30:
    print("It is a hot day")
    print("Drink plenty of water")
elif int(temperature) > 20:
    print("It is a nice day")
elif int(temperature) > 10:
    print("It is a bit cold")
else:
    print("It is cold outside")
