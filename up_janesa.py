print("===== PEMESANAN TIKET BIOSKOP =====")

while True:
    nama = input("\nMasukkan nama pelanggan: ")

    print("\nJenis Tiket:")
    print("1. Reguler  - Rp35.000")
    print("2. VIP      - Rp50.000")
    print("3. Premium  - Rp75.000")

    jenis = input("Pilih jenis tiket: ")
    jumlah = int(input("Masukkan jumlah tiket: "))

    # Menentukan harga tiket
    if jenis == "1":
        jenis_tiket = "Reguler"
        harga = 35000

    elif jenis == "2":
        jenis_tiket = "VIP"
        harga = 50000

    elif jenis == "3":
        jenis_tiket = "Premium"
        harga = 75000

    else:
        print("Jenis tiket tidak tersedia!")
        continue

    # Menghitung total harga
    total = harga * jumlah

    # Mengecek diskon
    if jumlah > 3:
        diskon = total * 10 / 100
    else:
        diskon = 0

    pembayaran = total - diskon

    # Menampilkan hasil pemesanan
    print("\n===== DETAIL PEMESANAN =====")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", jenis_tiket)
    print("Jumlah Tiket   :", jumlah)
    print("Harga Total    : Rp", total)
    print("Diskon         : Rp", int(diskon))
    print("Total Bayar    : Rp", int(pembayaran))

    print("============================")

    # Mengulang pemesanan
    ulang = input("\nApakah ingin melayani pelanggan lain? (ya/tidak): ")

    if ulang == "tidak":
        print("Terima kasih sudah memesan tiket")
        break

    elif ulang == "ya":
        continue

    else:
        print("Pilihan tidak valid!")
        break