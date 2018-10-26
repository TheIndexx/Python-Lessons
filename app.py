firstName = input("Enter your first name: ")
if not firstName:
    firstName = input("Type something: ")
lastName = input("Enter your last name: ")
if not lastName:
    lastName = input("Type something: ")
addressLine1 = input("Enter your address(line 1): ")
if not addressLine1:
    addressLine1 = input("You must type something: ")
addressLine2 = input("Enter your address line(second line, don't have to type something: ")
city = input("Enter what city you live in: ")
if not city or len(city)>50:
    city = input("You must type something or it was over 50 characters: ")
state = input("Enter the abbreviated form of your state aka TX: ")
if not state or len(state)>2:
    state = input("You must type something or it was over 2 letters: ")
zipCode = input("Enter your Zip Code: ")
if not zipCode:
    zipCode = input("You must type something: ")
print(firstName+" "+lastName)
print(addressLine1)
if addressLine2:
    print(addressLine2)
print(city+" "+state+", "+zipCode)
