# Menghitung luas dan keliling persegi panjang 

panjang = float(input("Masukkan panjang persegi panjang (m): "))
lebar = float(input("Masukkan lebar persegi panjang (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas persegi panjang    : {luas} m2")
print(f"Keliling persegi panjang: {keliling} m")

# Trace Table (input: panjang = 10, lebar = 20)
# | Baris | Panjang | Lebar | Luas | Keliling | Output 
# |-------|---------|-------|------|----------|--------
# | 3     | 10.0    |       |      |          |        
# | 4     | 10.0    | 20.0  |      |          |        
# | 6     | 10.0    | 20.0  |200.0 |          |        
# | 7     | 10.0    | 20.0  |200.0 |60.0      |        
# | 9     | 10.0    | 20.0  |200.0 |60.0      |Luas persegi panjang: 200.0 m2        
# | 10    | 10.0    | 20.0  |200.0 |60.0      |Keliling persegi panjang: 60.0 m        