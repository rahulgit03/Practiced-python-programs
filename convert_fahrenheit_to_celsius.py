def convert_fahrenheit_to_celsius(f):
    c=(f - 32) * 5/9
    return c
c=float(input('enter celsius :'))
result=convert_fahrenheit_to_celsius(c)
print(result)
