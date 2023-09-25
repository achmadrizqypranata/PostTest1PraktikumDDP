def login():

    while True:
        coverstrip = '-'*50
        print(coverstrip)
        nama = input("Masukkan Nama Anda: ")
        nim = int(input("Masukkan NIM Anda: "))
        print(coverstrip)
        print("List Kelas")
        print("1. Sistem Informasi A ")
        print("2. Sistem Informasi B ")
        print(coverstrip)
        kelas = input("Pilih Kelas Anda: ")
        if kelas == "1":
            kelas = ("Sistem Informasi A")
        elif kelas == "2":
            kelas = ("Sistem Informasi B")
        else:
            print("Anda Tidak Memilih Kelas.")
        password = input("Buat Password Anda: ")
        confirmPass = input("Masukkan Password Anda: ")  
        if password == confirmPass:
            print(coverstrip)
            print(f"Selamat Datang {nama} dengan NIM {nim} dari kelas {kelas} di Program Menghitung Nilai Konversi Satuan Massa kilogram (kg).")
            print(coverstrip)
            break
        else:
            print("Login Anda ditolak, Silahkan Coba lagi")

def menghitung():
    lanjut = True
    while lanjut :
        coverstrip = '-'*50
        print("Pilih satuan massa yang ingin Anda konversikan:")
        print("1. Pounds (lb)")
        print("2. Ons (ons)")
        print("3. Gram (g)")
        print(coverstrip)

        pilihan = input("Masukkan nomor pilihan yang ingin Anda konversikan: ")

        if pilihan == "1":
            berat_pounds = float(input("Masukkan berat dalam pounds (lb): "))
            berat_kilogram = berat_pounds * 0.45359237  # 1 pound = 0.45359237 kilogram
            print(f"{berat_pounds} pounds (lb) = {berat_kilogram} kilogram (kg)")
        elif pilihan == "2":
            berat_ons = float(input("Masukkan berat dalam ons (ons): "))
            berat_kilogram = berat_ons * 0.0283495  # 1 ons = 0.0283495 kg
            print(f"{berat_ons} ons (ons) = {berat_kilogram} kilogram (kg)")
        elif pilihan == "3":
            berat_gram = float(input("Masukkan berat dalam gram (g): "))
            berat_kilogram = berat_gram / 1000  # 1000 gram = 1 kg
            print(f"{berat_gram} gram (g) = {berat_kilogram} kilogram (kg)")
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3 untuk memilih satuan massa yang ingin dikonversikan.")
            print(coverstrip)
        quit = input("Apakah kamu ingin menghitung lagi (y / n)? ")
        if quit == "n" or quit == "N":
            lanjut = False
            
            coverstrip = '-'*50
            print(coverstrip)
            print("Terima kasih telah menggunakan Program Menghitung Nilai Konversi Satuan Massa kilogram (kg).")
            print(coverstrip)

login()
menghitung()
