# variable dan tipe data
nama_mhs = input("Masukkan Nama:")
kelas = input ("Kelas :")

#rata_rata = (nilai_algoritma + nilai_agama + nilai_basisdata + nilai_bahasaindonesia + nilai_logikainformatika + nilai_pancasila + nilai_bahasinggris)
#print(rata-rata)
nilai_a = int(input("Masukkan Nilai Algoritma:"))
nilai_b = int(input("Masukkan Nilai Agama:"))
nilai_c = int(input("Masukkan Nilai Basis Data:"))
nilai_d = int(input("Masukkan Nilai Bahas Indonesia:"))
nilai_e = int(input("Masukkan Nilai Logika Informatika:"))
nilai_f = int(input("Masukkan Nilai Pancasila:"))
nilai_g = int(input("Masukkan Nilai Bahas Inggris:"))
rata_rata = (nilai_a+nilai_b+nilai_c+nilai_d+nilai_e+nilai_f+nilai_g) / 7


print (rata_rata)

if rata_rata>=80 and rata_rata<=100:
    #kondisi jika terpenuhi
    #maka
    print("nilai : A")
elif rata_rata>=70 and rata_rata<=80:
    print("nilai : B")
elif rata_rata>=50 and rata_rata<=70:
    print("nilai C")
elif rata_rata>=30 and rata_rata<=50:
    print("nilai D")
else: 
    #cukup menampilkan hasil
    #maka
    print("Nilai E")




