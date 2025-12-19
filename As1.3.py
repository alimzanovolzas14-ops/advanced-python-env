A = input("Enter a real number: ") 
integer_part, fractional_part = A.split('.') 
new_number = float(fractional_part) + float(integer_part) / 100 
print(new_number) 
