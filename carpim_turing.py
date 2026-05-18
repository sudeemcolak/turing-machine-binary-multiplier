class TuringMachine:
    def __init__(self, bant):
        self.bant = list(bant)
        self.kafa = 0
        self.durum = "q0"
        self.adim_sayisi = 0
        self.shift_miktari = 0 #multiplier'ın kaç bit kaydırılacağını takip etmek için bir sayaç
        self.partial_sonuclar = []
        self.sonuc_binary = ""


    def saga_kay(self):
        self.kafa += 1

        if self.kafa >= len(self.bant):
            self.bant.append("_")

    def sola_kay(self):
        if self.kafa > 0:
            self.kafa -= 1

    def sembol_oku(self):
        return self.bant[self.kafa]

    def sembol_yaz(self, symbol):
        self.bant[self.kafa] = symbol

# Turing makinesi için çarpma işlemi kurallarını tanımlayalım.
    def operandlari_ayir(self):

        print("\n= Operand Ayırma Başladı =")

        while self.sembol_oku() != "*":

            okunan = self.sembol_oku()

            self.durum_goster(
                okunan=okunan,
                yazilan=okunan,
                hareket="R")

            self.saga_kay()


            if self.kafa >= len(self.bant):  
                break

        self.durum = "q1" # '*' sembolü bulma durumu q1 oldu.

        print("\n'*' bulundu!")
        print("Operandlar başarıyla ayrıldı.")

        print("\nSol taraf -> Birinci sayı")
        print("Sağ taraf -> İkinci sayı")

# Çarpmanın ikinci asamasi

    def multiplier_sonuna_git(self):

        self.durum = "q2" # multiplier'ın sonuna gitme durumu q2 oldu.

        print("\n= Multiplier Sonuna Gidiliyor =")

        # '=' karakterine kadar ilerle
        while self.sembol_oku() != "=":

            okunan = self.sembol_oku()

            self.durum_goster(
                okunan=okunan,
                yazilan=okunan,
                hareket="R")

            self.saga_kay()


        print("\n'=' bulundu.")

        print("Bir adım sola gidiliyor...") 
        
        self.sola_kay()


        print("\nMultiplier'ın en sağ bitine ulaşıldı.")
    
# multiplier bitini okuma
    def bit_kontrol(self):

        self.durum = "q3" # bit okuma durumu q3 oldu.

        print("\n= Bit Kontrolü Başladı =")

        bit = self.sembol_oku() 

        if bit == "1":

            self.durum_goster(
                okunan=bit,
                yazilan=bit,
                hareket="S")
            
            self.shift_islemi()

        elif bit == "0":

            self.durum_goster(
                okunan=bit,
                yazilan=bit,
                hareket="S")

        else:

            print("HATA: Geçersiz bit!")
            self.durum = "q_reject"


    def shift_islemi(self):

        self.durum = "q4" # shift işlemi durumu q4 oldu.

        print("\n= Shift İşlemi Başladı =")

        bit = self.sembol_oku()

        if bit == "1":

            yildiz_index = self.bant.index("*")
            birinci_sayi = "".join(self.bant[:yildiz_index])

            shiftli_sayi = birinci_sayi + ("0" * self.shift_miktari)

            self.durum_goster(
                okunan=bit,
                yazilan=shiftli_sayi,
                hareket="S"
            )

            print(f"Shift Sonucu: {shiftli_sayi}")

            self.partial_sonuclar.append(shiftli_sayi)

        else:
            print("Bit = 0 olduğu için shift işlemi yapılmadı.")

    def multiplier_isle(self):

        print("\n= Multiplier İşleniyor =")
        self.shift_miktari = 0

        # '*' karakterine ulaşana kadar devam et
        while self.sembol_oku() != "*":

            # q3 -> bit kontrol
            self.bit_kontrol()

            # Bir sola kay
            self.sola_kay()

            # Shift miktarını artır
            self.shift_miktari += 1




        print("\nMultiplier tamamen işlendi.")

    def partial_topla(self):

        self.durum = "q5" # kısmi sonuçları toplama durumu q5 oldu.

        print("\n= Partial Sonuçlar Toplanıyor =")

        toplam = 0

        for binary_sayi in self.partial_sonuclar:

            print(f"\nToplanan sayı: {binary_sayi}")

            decimal_deger = int(binary_sayi, 2)

            print(f"Decimal karşılığı: {decimal_deger}")

            toplam += decimal_deger

        print(f"\nToplam decimal sonuç: {toplam}")

        self.sonuc_binary = bin(toplam)[2:]

        print(f"Binary sonuç: {self.sonuc_binary}")

    def sonucu_banta_yaz(self):

        self.durum = "q6" # sonucu banda yazma durumu q6 oldu.

        print("\n= Sonuç Banda Yazılıyor =")

        esittir_index = self.bant.index("=")

        # '=' sonrası temizleniyor
        self.bant = self.bant[:esittir_index + 1]

        # Sonucu banda ekle
        for bit in self.sonuc_binary:

            self.bant.append(bit)

        self.durum_goster(
            okunan="=",
            yazilan=self.sonuc_binary,
            hareket="S")

    def kabul_et(self):

        self.durum = "q_accept" # kabul durumunu q_accept olarak tanımlıyoruz.

        print("\n= MAKİNE KABUL DURUMUNDA =")

        self.durum_goster(
            okunan="=",
            yazilan=self.sonuc_binary,
            hareket="S")

    def reddet(self):

        self.durum = "q_reject" # reddetme durumunu q_reject olarak tanımlıyoruz.

        print("\n= HATALI GİRDİ =")

        self.durum_goster(
            okunan="=",
            yazilan=self.sonuc_binary,
            hareket="S")

    def durum_goster(self, okunan="", yazilan="", hareket=""):

        self.adim_sayisi += 1

        print("\n----------------------------")
        print(f"[ADIM {self.adim_sayisi}]")
        print(f"Durum          : {self.durum}")
        print(f"Okunan Sembol  : {okunan}")
        print(f"Yazılan Sembol : {yazilan}")
        print(f"Hareket        : {hareket}")

        bant_str = "".join(self.bant)

        print(f"Bant           : {bant_str}")

        print("                 " + " " * self.kafa + "^")

        print("----------------------------")

def binary_kontrol(sayi): # girişin 1-0lardan oluştuğu kontrolü
    if sayi == "":
        return False

    for karakter in sayi:
        if karakter not in ["0", "1"]:
            return False

    return True
    


# test kodları
num1 = input("Birinci binary sayı: ")
num2 = input("İkinci binary sayı: ")

if not binary_kontrol(num1) or not binary_kontrol(num2):

    print("HATA: Sadece binary sayı girilebilir!")

else:

    bant = f"{num1}*{num2}="

    tm = TuringMachine(bant)
    tm.operandlari_ayir()
    tm.multiplier_sonuna_git()
    tm.multiplier_isle()
    tm.partial_topla()
    tm.sonucu_banta_yaz()
    tm.kabul_et()