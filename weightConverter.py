weight = int(input("Enter the weight to convert: "))
units = input("(K)kg or (L)lbs: ")

if units.upper() == "K":
    converted = weight/0.45
    print("Weigh tn in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
