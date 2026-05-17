# Turing Makinesi ile Binary Çarpma Hesaplayıcı

Bu proje, Python programlama dili kullanılarak geliştirilmiş tek bantlı bir Turing Makinesi simülatörüdür. Program, iki binary (ikili) sayıyı “shift & add” yöntemi kullanarak çarpmaktadır.

## Projenin Amacı

Bu çalışmanın amacı:

* Turing Makinesi mantığını simüle etmek
* Binary sayı sistemi üzerinde işlem gerçekleştirmek
* Operand ayrıştırma işlemini modellemek
* Durum tabanlı algoritma tasarımı yapmak
* Çarpma işlemini adım adım göstermek

olarak belirlenmiştir.

---

# Kullanılan Teknolojiler

* Python
* Tek Bantlı Turing Makinesi Modeli

---

# Programın Özellikleri

Program aşağıdaki işlemleri gerçekleştirmektedir:

* Kullanıcıdan iki adet binary sayı alma
* Girdilerin yalnızca 0 ve 1 içerdiğini kontrol etme
* Bant yapısını oluşturma
* `*` karakteri ile operandları ayırma
* `=` karakterinden sonra sonucu yazma
* Shift & Add yöntemi ile binary çarpma yapma
* Her adımda:

  * mevcut durum
  * okunan sembol
  * yazılan sembol
  * kafa hareketi
  * bant içeriği

bilgilerini ekrana yazdırma.

---

# Bant Formatı

Program girdileri aşağıdaki bant formatına dönüştürmektedir:

```text
11*10=
```

Burada:

* `*` → iki operandı ayırır
* `=` → sonuç alanını belirtir

---

# Kullanılan Durumlar

| Durum    | Açıklama                                    |
| -------- | --------------------------------            |
| q0       | Başlangıç, Operand ayırma durumu            |
| q1       | Operand doğrulama durumu                    |
| q2       | Multiplier sonuna gitme durum               |
| q3       | Bit kontrol durumu                          |
| q4       | Shift işlemi durumu                         |
| q5       | Partial sonuçları toplama durumu            |
| q6       | Sonucu banda yazma durumu                   |
| q_accept | Kabul durumu                                |
| q_reject | Hata durumu                                 |

---

# Örnek Çalışma

## Girdi

```text
Birinci binary sayı: 11
İkinci binary sayı: 10
```

## Bant

```text
11*10=
```

## Çıktı

```text
110
```

---

# Çalışma Mantığı

Program aşağıdaki adımları takip eder:

1. Bant üzerinde `*` karakteri bulunur
2. Operandlar birbirinden ayrılır
3. Multiplier’ın en sağ bitinden başlanır
4. Her bit için:

   * Bit = 1 → shift işlemi yapılır
   * Bit = 0 → işlem yapılmadan devam edilir
5. Partial sonuçlar toplanır
6. Sonuç banda yazılır
7. Makine kabul durumunda durur


