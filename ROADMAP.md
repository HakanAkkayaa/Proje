# ROADMAP.md: Python ile OSINT Destekli Ağ Taraması ve Cihaz Analizi Geliştirme Rehberi

## Giriş
Bu yol haritası, Python programlama dili kullanılarak geliştirilen OSINT destekli ağ tarama ve cihaz analiz sisteminin nasıl yapılandırılacağını, geliştirileceğini ve test edileceğini detaylı olarak açıklar. Bu proje, ağdaki cihazları MAC adresi üzerinden tanımlayarak üretici bilgilerini OUI (Organizationally Unique Identifier) veritabanı ile eşleştirir, cihaz türünü tahmin eder ve cihazlara ait temel açık port bilgilerini tespit eder. 

**Uyarı**: Bu yazılım yalnızca eğitim, laboratuvar ve test ortamlarında kullanılmalıdır. Yetkisiz ağlara karşı kullanımı etik dışı ve yasa dışıdır.

## Amaç
- Ağ üzerindeki cihazları ARP protokolü ile taramak.
- MAC adreslerinden üreticiyi belirlemek (OUI).
- OSINT teknikleriyle cihaz türünü tahmin etmek.
- Ping atarak cihazın erişilebilirliğini kontrol etmek.
- Belirli portlara tarama yaparak servis bilgileri elde etmek.
- Sonuçları kullanıcı dostu bir GUI arayüzünde listelemek.

## Ön Koşullar
- **Python 3.x**
- **Kütüphaneler**:
  - `scapy`: Ağ paketleri oluşturma ve analiz → `pip install scapy`
  - `socket`: Port taraması için
  - `subprocess`, `platform`: Ping işlemleri için
  - `customtkinter`: Modern kullanıcı arayüzü → `pip install customtkinter`
  - `tkinter.ttk`: Tablo görünümü
- **Veri Dosyası**:
  - `oui.txt`: MAC üretici listesini içeren OUI veritabanı (IEEE kaynaklı)

## Test Ortamını Kurma
1. **Sistem Gereksinimleri**:
   - Python 3 yüklü bir Linux/Windows sistemi.
   - Sudo yetkisine sahip kullanıcı (Scapy için gerekebilir).

2. **Ağ Yapısı**:
   - Uygulama, yalnızca aynı yerel ağdaki cihazları tarar (örnek: `192.168.1.0/24`).
   - Herhangi bir router ya da WiFi ağında kullanılabilir.



### MAC Adresinden Vendor Tespiti
```python
mac_prefix = mac.upper().replace("-", ":")[:8].lower()
vendor = oui_veritabani.get(mac_prefix)
```

### OSINT Tabanlı Cihaz Türü Tahmini
```python
if "apple" in vendor: return "Telefon/Tablet"
if "dell" in vendor: return "Bilgisayar"
if "epson" in vendor: return "Yazıcı"
```

### Ping Cihaz Durumu Kontrolü
```python
subprocess.run(["ping", "-c", "1", ip])
```
### Port Taraması
```python
for port in [80, 443, 22, 3389]:
    socket.connect_ex((ip, port))
```

## Arayüz (GUI)

- `CustomTkinter` kullanılarak kullanıcı dostu karanlık tema arayüzü tasarlandı.
- Arayüz bileşenleri:
  - IP aralığı giriş kutusu
  - Tarama başlatma butonu
  - İlerleme çubuğu
  - Sonuçların listelendiği tablo
- Gösterilen bilgiler:
  - **IP Adresi**
  - **MAC Adresi**
  - **Marka (Vendor)**
  - **Cihaz Türü**
  - **Durum (Ping sonucu)**
  - **Açık Portlar**

---

## Gelişmiş Geliştirmeler

1. **Firmware OSINT Özelliği (Opsiyonel)**  
   Tanımlanan markaya göre internette firmware dosyaları arayarak analiz için indirme bağlantıları sunulabilir.

2. **CVE Entegrasyonu (Opsiyonel)**  
   Markaya göre CVE API (örneğin [NVD](https://nvd.nist.gov/)) kullanılarak bilinen güvenlik açıkları listelenebilir.

3. **Tarama Geçmişi Kaydı**  
   Tarama sonuçları bir `results.csv` dosyasına yazılarak analiz ve karşılaştırma yapılabilir.

4. **Gelişmiş Port Taraması**  
   `nmap` benzeri bir yapı ile daha fazla port taranabilir, servis tanıma (banner grabbing) eklenebilir.

---

## Test Senaryoları

- **Ağ Taraması**: IP aralığı girilir, cihazlar listelenmeli.
- **MAC–Vendor Eşleşmesi**: Üretici doğru eşleşmeli.
- **Cihaz Türü Tahmini**: Doğru sınıflandırma yapılmalı.
- **Ping Testi**: Cevap veren cihazlar “Çevrimiçi” görünmeli.
- **Port Tarama**: Açık portlar doğru listelenmeli.

---

## Güvenlik ve Etik Önlemler

- Yalnızca kendi ağınızda kullanın.
- Üçüncü kişilere ait cihazları izinsiz taramayın.
- Tarama yükünü düşük tutun.
- Veriler kaydediliyorsa güvenli bir şekilde saklanmalıdır.

---

## Sonuç

Bu yol haritası, Python ve OSINT teknikleri kullanılarak geliştirilen ağ tarama uygulamasının tüm yapı taşlarını kapsamlı bir şekilde açıklamıştır. Eğitim, araştırma ve laboratuvar testleri için ideal olan bu proje, siber güvenlik, cihaz tanıma ve ağ analiz konularında pratik bilgi sağlar. Gerçek dünyada kullanılmadan önce yasal ve etik çerçevede test edilmelidir.
