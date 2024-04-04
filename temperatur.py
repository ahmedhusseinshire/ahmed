# # 

# x = float(input("enter any whole number : "))

# equation = ((3 * x * x * x) - (2 * x * x) + (3 * x) - 1)

# print("y =",equation)


print("welcome to temperature converter \n")

choice_converter =input("what type of convertion do you want? Type C to convert ferh to celsious or F to convert celsious to freh : ").upper()

if choice_converter == "c".upper():

    temperature_in_celcius = int(input("Enter value of temperature in celcius :"))
    result = int(temperature_in_celcius - 32) * 5/9
  
    print(f"temperature is {result} celcius")
elif choice_converter == "f".upper():

    temperature_in_ferh = int(input("Enter value of temperature in ferh :"))
    result = int(temperature_in_ferh - 32) * 5/9
  
    print(f"temperature is {result} celcius")

else:
    print("ACHA UJINGA HUJUI KUSOMA MAELEKEZO")
    
    
print("GET OUT OF MY PROJECT") 

    