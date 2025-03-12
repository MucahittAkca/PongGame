# Pong Oyunu 🏓

Bu proje, klasik Pong arcade oyununun Python ile geliştirilmiş modern bir versiyonudur. İki oyuncunun karşılıklı oynadığı bu oyunda, amacınız topu rakip tarafa geçirmek ve puan kazanmaktır.

## 🎮 Özellikler

- İki kişilik oyun modu
- Dinamik top hızı (çarpışmalarda artar)
- Skor takip sistemi
- Şık ve basit arayüz
- Kolay kontroller

## 🛠️ Gereksinimler

- Python 3.x
- Python Turtle modülü (standart kütüphanede mevcuttur)

## 📥 Kurulum

1. Projeyi bilgisayarınıza klonlayın:
```bash
git clone https://github.com/MucahittAkca/PongGame.git
```

2. Proje dizinine gidin:
```bash
cd PongGame
```

3. Oyunu başlatın:
```bash
python main.py
```

## 🕹️ Nasıl Oynanır?

### Kontroller:
- **Sağ Oyuncu:**
  - Yukarı Ok Tuşu: Küreki yukarı hareket ettirir
  - Aşağı Ok Tuşu: Küreki aşağı hareket ettirir

- **Sol Oyuncu:**
  - W Tuşu: Küreki yukarı hareket ettirir
  - S Tuşu: Küreki aşağı hareket ettirir

### Oyun Kuralları:
- Top rakip tarafa geçerse 1 puan kazanırsınız
- Top küreklere çarptıkça hızı artar
- Oyun sonsuza kadar devam eder, istediğiniz zaman pencereyi kapatarak bitirebilirsiniz

## 📁 Proje Yapısı

- `main.py`: Ana oyun dosyası
- `tahta.py`: Kürek kontrolü ve yönetimi
- `top.py`: Top hareketi ve fizik hesaplamaları
- `scoreboard.py`: Skor takip sistemi

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun
