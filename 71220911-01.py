jam_awal = int(input("Jam Awal = "))
menit_awal = int(input("Menit Awal = "))

jam_akhir = int(input("Jam Akhir = "))
menit_akhir = int(input("Menit Akhir = "))

total_awal = jam_awal * 60 + menit_awal
total_akhir = jam_akhir * 60 + menit_akhir

selisih = total_akhir - total_awal
print ("Selisihnya adalah", selisih, "menit")
