def tekrar():
    print("\n"+("-"*50)+"\n")
    dboyut = float(input("Dosyanın Boyutunu Giriniz (GB): "))
    dhiz = float(input("Dosyanın İndirme Hızını Giriniz (MB): "))

    dboyutmb = dboyut * 1024
    dhizsan = dboyutmb / dhiz

    dhizsaat = int(dhizsan // 3600)
    dhizsaatkal = dhizsan % 3600

    dhizdakika = int(dhizsaatkal // 60)
    dhizdakikakal = dhizsaatkal % 60

    print()

    if dhizsaat == 0 and dhizdakika == 0:
        print(f"\t+{"-"*63}+\n\t   Dosyanız {dhizdakikakal:.1f} Saniye İçinde İnecektir.\n\t+{"-"*63}+")
    elif dhizsaat == 0:
        print(f"\t+{"-"*63}+\n\t   Dosyanız {dhizdakika} Dakika Ve {dhizdakikakal:.1f} Saniye İçinde İnecektir.\n\t+{"-"*63}+")
    else:
        print(f"\t+{"-"*63}+\n\t   Dosyanız {dhizsaat} Saat, {dhizdakika} Dakika Ve {dhizdakikakal:.1f} Saniye İçinde İnecektir.\n\t+{"-"*63}+")

    print()

    sorutek = input("Dosya Hızını Tekrar Öğrenmek İstermisiniz?(E/H): ")
    if sorutek == "E" or sorutek == "e":
        tekrar()
    else:
        print("Tekrar Görüşmek Üzere!"+"\n"+("-"*50))
        
tekrar()
