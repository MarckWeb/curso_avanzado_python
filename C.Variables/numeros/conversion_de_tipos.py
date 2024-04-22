# int()-. convierte un numero string a numero
# string() -. convierte un numero a string
# float() -.  convierte un numero  a float
# bool() -. basado en truthy u falsy convierte un valor a true o false, falsy son considerado ("", 0, none)


parsecs = 11
años_luz = parsecs * 3.26
print(str(parsecs) + " parsecs son " + str(años_luz) + " años luz")

print(int('12355'))
print(str(255))
print(float(10))

print(bool(1))
print(bool(1.22))
print(bool('falso'))
print(bool('  '))
print(bool(0))
print(bool(""))
