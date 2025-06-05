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
| [Hilal Paksoy]  | [2320191085] | Proje Yardımcısı |
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
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |     buu kendi projeme nasıl uyarlayabilirim


---

## Installation / *Kurulum*

1. **Python 3.10** 
kurulu olup olmadığını kontrol edin:

   ```bash
   python --version
   ```

3. **Pip** 
kurulu olup olmadığını kontrol edin:

   ```bash
   pip --version
   ```

4. **Install Necessary Packages / Gerekli Paketleri Yükleyin***
    Aşağıdaki komut ile ihtiyaç duyulan kütüphaneleri yükleyin:
    Install the required libraries with the following command:

   ```bash
   pip install scapy
   pip install customtkinter
   ```
4. **Npcap**
  https://nmap.org/npcap/

5. **Tkinter**
Python ile birlikte gelen GUI kütüphanesi

6.**Download Project Files, Clone Project / Proje Dosyalarını İndirin, Projeyi Klonlayın***
    GitHub üzerinden projeyi klonlayın veya ZIP olarak indirin:
    Clone the project from GitHub or download it as a ZIP:
   ```bash
   git clone https://github.com/keyvanarasteh/Project.git
   cd Project
   ```
7.  **Launch the App / Uygulamayı Başlatın***
   Aşağıdaki komutla uygulamayı başlatabilirsiniz:
   You can start the application with the following command: 
   ```bash
   python app.py
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python app.py

```

**Steps**:  
1. Launch the application.  
2. REnter the IP range (e.g., 192.168.1.0/24) in the input field.  
3. Click the "Ağı Tara" (Scan Network) button.
4. The results will appear in the table below the GUI: IP, MAC, vendor, device type, ping status, and open ports.

*Adımlar*:  
1. Uygulamayı başlatın.
2. IP aralığını girin (örneğin: 192.168.1.0/24).
3. "Ağı Tara" butonuna tıklayın.
4. Cihazlara ait IP, MAC, marka, cihaz türü, ping durumu ve açık portlar tablo şeklinde listelenir.
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

Licensed under the [MIT License](LICENSE).  
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
