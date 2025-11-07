def görev_dosyası_oku(görevdosyası):
    with open(görevdosyası, "r", encoding="utf-8") as f:
        for i, satir in enumerate(f, start=1):
            görevler[i] = satir.strip()
    return görevler

def görev_dosyası_yaz(gorevler,görevdosyası):
    with open(görevdosyası, "w", encoding="utf-8") as f:
        for k in sorted(gorevler.keys()):  # sözlükteki her bir key döndürülür ve value değerleri satır satır yazdırılır
            f.write(gorevler[k] + "\n")

def görev_ekle(gorev, yenigörev):
    if yenigörev:
        leng = len(gorev)
        gorev[leng+1] = yenigörev     # sözlüğün sonuna eklenmesi için uzunluğundan 1 fazla olan pozisyona ekleme yapıyoruz.
        print("'" + str(yenigörev) + "'" , "eklendi")
    else:
        print("Bir görev girmediniz.")
    return gorev

def görev_listele(gorev):

    if len(gorev) == 0:
        print("Henüz göreviniz bulunmuyor.")
    else:
        print("---Görev Listeniz---")
        for k, v in gorev.items():
            print(str(k) +  ":", v)
        print("--------------------")

def görev_düzenle(gorev,gorevNum):
    if gorevNum.isdigit():
        gorevNum = int(gorevNum)
        if gorevNum in list(gorev.keys()):
            yenigörev = input("Yeni görevi giriniz: ")
            if yenigörev == "":
                print("Lütfen bir görev giriniz.")
                görev_düzenle(gorev)
            else:
                gorev[gorevNum] = yenigörev
                print(str(gorevNum) + " numaralı görev düzenlendi")

        else:
            print("Bu numarada bir görev bulunmuyor.")
    else:
        print("Geçerli bir sayı girmediniz.")

    return gorev



def görev_sil(gorev, gorevNum):
    gorevNum = int(gorevNum)
    if gorevNum in list(gorev.keys()):
        del gorev[gorevNum]
        gorev = {i + 1: v for i, v in enumerate(gorev.values())}
        print(str(gorevNum) + " numaralı görev silindi.")
    else:
        print("Bu numarada bir görev bulunmuyor.")

    return gorev

num = 0
görevler = {}

görev_dos = input("\nMevcut bir görev dosyanız varsa giriniz yoksa 0 yazınız: ")

if görev_dos != "0":
    try:
        görevler = görev_dosyası_oku(görev_dos)
        print("Görevleriniz yüklendi.")

    except FileNotFoundError:
        print(f"Hata: '{görev_dos}' bulunamadı!")
        print("Görev yüklenmeden devam ediliyor.")
        görev_dos = "yeniDosya.txt"

else:
    print("Görev yüklenmeden devam ediliyor.")
    görev_dos = "yeniDosya.txt"


print("\n-------Görev Listenize Hoşgeldiniz!-------")

print("MENU:\n"
      "1. Görevleri Listele\n"
      "2. Yeni Görev Ekle\n"
      "3. Görev Düzenle\n"
      "4. Görev Sil\n"
      "5. Çıkış")


while num != "5":
    num = input("\nLütfen 1-5 arası bir seçim yapınız: ")

    if num == "1":
        görev_listele(görevler)

    elif num == "2":
        yenigörev = input("Yeni görev giriniz: ")
        görevler = görev_ekle(görevler,yenigörev)
        görev_dosyası_yaz(görevler,görev_dos)

    elif num == "3":
        gorevNum = input("Hangi numaralı görevi düzenlemek istiyorsunuz?: ")
        görevler = görev_düzenle(görevler, gorevNum)
        görev_dosyası_yaz(görevler, görev_dos)

    elif num == "4":
        gorevNum = input("Hangi numaralı görevi silmek istiyorsunuz?: ")
        görevler = görev_sil(görevler, gorevNum)
        görev_dosyası_yaz(görevler, görev_dos)

    elif num == "5":
        print(f"Görevleriniz {görev_dos} dosyasına kaydedilmiştir.\nÇıkış yapılıyor...")


    else:
        print("Lütfen menüden 1-5 arası bir seçim yapınız")