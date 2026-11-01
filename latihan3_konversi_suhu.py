# Program Konversi Suhu Dari Celsius Ke Fahrenheit Dan Kelvin

celsius = float(input("Masukkan suhu (Celsius): "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} F")
print(f"Suhu dalam Kelvin: {kelvin:.2f} K")