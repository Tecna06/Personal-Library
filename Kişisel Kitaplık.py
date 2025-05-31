
# Kişisel Kitaplık Uygulaması

kitaplik = []  # Kitapları depolayacak liste

def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar adı: ")
    kitap = {"kitap_adi": kitap_adi, "yazar": yazar}
    kitaplik.append(kitap)
    print(f"'{kitap_adi}' başarıyla eklendi!\n")

def kitaplari_goster():
    if len(kitaplik) == 0:
        print("Kitaplık boş.\n")
    else:
        print("Kitaplığındaki kitaplar:")
        for i, kitap in enumerate(kitaplik, start=1):
            print(f"{i}. {kitap['kitap_adi']} - {kitap['yazar']}")
        print("")

while True:
    print("1. Kitap ekle")
    print("2. Kitapları göster")
    print("3. Çıkış")
    secim = input("Seçiminiz: ")

    if secim == "1":
        kitap_ekle()
    elif secim == "2":
        kitaplari_goster()
    elif secim == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.\n")
