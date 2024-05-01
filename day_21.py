
# f-string in python.
# string formatting in python

letter="Hey my name is {} and I am from {}."
country="Nepal"
name="Pramod"
print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}.") # this is f-string

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}.")

txt="For only {price:.2f} dollars!"
print(txt.format(price=49.56452346))

price=79.436363
txt=f"For only {price:.2f} dollars!"
print(txt)

print(type(f"{2*3}"))
