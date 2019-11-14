print ("---- MENU ----")
print ("[1.] Menambah Data Mahasiswa")
print ("[2.] Mengubah Data Mahasiswa")
print ("[4.] Mengapus Data Mahasiswa ")
print ("[4.] Melihat Seluruh Data Mahasiswa")
print ("[4.] Keluar")
pilih = input("pilih : ")

nama = {"abdul", "sidiq", "agus"}

for kelas in nama:
    print(kelas)
print("-----------------------\n")


nama.add("Agis")
for kelas in nama:
    print(kelas)
print("-----------------------\n")


nama.remove("abdul")
for kelas in nama:
    print(kelas)
print("-----------------------\n")
print("melihat semua nama yang terdaftar")
print(nama)
print("5. Keluar")