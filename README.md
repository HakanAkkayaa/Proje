<div align="center">
  <img src="https://img.shields.io/github/languages/count/keyvanarasteh/Project?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/keyvanarasteh/Project?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/keyvanarasteh/Project?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/keyvanarasteh/Project?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# 🔍 Akıllı Ağ Tarayıcı 
  
Bu Python tabanlı gelişmiş ağ tarayıcı uygulaması, bağlı cihazları anlık olarak tespit eder, IP ve MAC adreslerini listeler, üretici markalarını belirler, cihaz türünü tahmin eder ve açık portlarını tarar. Modern bir grafik arayüz (GUI) ile sunulan bu araç sayesinde, ağını analiz etmek sadece tek bir tık uzağında!

---

## Features / *Özellikler*

- **Network Scanning:** Scans your local network to discover active devices with their IP and MAC addresses.

  *Ağ Taraması:* Yerel ağdaki aktif cihazları IP ve MAC adresleriyle birlikte tarar.

- **Vendor & Device Type Detection:** Identifies the manufacturer and estimates the type of each device (PC, phone, printer, etc.) using MAC address lookup.

  *Marka ve Cihaz Türü Tespiti:* MAC adresiyle üretici markasını bulur ve cihazın türünü tahmin eder (PC, telefon, yazıcı vb.).

- **Open Port Detection:** Detects commonly used open ports (like 80, 443, 22, 3389) on each device for basic vulnerability awareness.

  *Açık Port Tespiti:* Her cihazda yaygın kullanılan açık portları (80, 443, 22, 3389) tespit eder.

- **Real-Time GUI with Progress Bar:** Presents all results in a modern graphical interface with a live progress bar.

  *Gerçek Zamanlı Arayüz:* Tüm sonuçları canlı ilerleme çubuğu ile modern bir grafik arayüzde sunar.

- **Custom IP Range Support:** Allows scanning of any given IP range within or beyond local network (as permitted).

  *Özelleştirilebilir IP Aralığı Desteği:* Belirtilen herhangi bir IP aralığında tarama yapabilir.



---

## 👥 Takım Bilgileri

| İsim            | Öğrenci No   | Rol              |
| --------------- | ------------ | ---------------- |
| [Hakan Akkaya]  | [2320191089] | Proje Lideri |
| [Hilal Paksoy]  | [2320191015] | Proje Yardımcısı |
| [Betül Kaya]    | [2320191088] | Proje Yardımcısı |

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Aircrack Deep Dive      | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
