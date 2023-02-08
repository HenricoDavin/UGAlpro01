n = int(input("N = "))

upah_bruto = n * 8 *10000
pajak = upah_bruto * 5/100
upah_netto = upah_bruto - pajak

print ("Upah karyawan sebelum pajak: Rp. ", upah_bruto)
print ("Pajak upah karyawan: Rp. ", pajak)
print ("Upah karyawan setelah pajak: Rp. ", upah_netto)
