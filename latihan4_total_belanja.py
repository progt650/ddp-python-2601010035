# Program Menghitung Total Belanja Dengan PPN 11%

nama_barang = input("Masukkan nama barang: ")
harga_satuan = int(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

print(f"Nama Barang: {nama_barang}")
print(f"Subtotal   : {subtotal}")
print(f"PPN        : {ppn}")
print(f"Total Bayar: {total_bayar}")