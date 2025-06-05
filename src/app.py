import customtkinter as ctk
from scapy.all import ARP, Ether, srp
from tkinter import ttk
import platform
import subprocess
import socket

# OUI veritabanını belleğe al
oui_veritabani = {}
with open("oui.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if "(hex)" in line:
            parcalar = line.strip().split("\t")
            if len(parcalar) >= 2:
                mac_prefix = parcalar[0].strip().replace("-", ":").lower()
                vendor_name = parcalar[-1].strip()
                oui_veritabani[mac_prefix[:8]] = vendor_name

def get_vendor(mac):
    mac_prefix = mac.upper().replace("-", ":")[:8].lower()
    vendor = oui_veritabani.get(mac_prefix)
    if vendor:
        print(f"DEBUG | MAC: {mac} → Prefix: {mac_prefix} → Vendor: {vendor}")
        return vendor
    else:
        print(f"DEBUG | MAC: {mac} → Prefix: {mac_prefix} → Vendor: Bilinmiyor (prefix yok)")
        return "Bilinmiyor"

def tahmin_et(vendor):
    vendor = vendor.lower()

    if "apple" in vendor or "pegatron" in vendor or "hon hai" in vendor:
        return "Telefon/Tablet"

    telefonlar = ["samsung", "huawei", "xiaomi", "apple", "oppo", "vivo", "realme", "hon hai", "foxconn", "oneplus", "pegatron", "macbook", "iphone", "ipad"]
    bilgisayarlar = ["dell", "hp", "lenovo", "msi", "asus", "acer", "gigabyte", "giga-byte", "micro-star", "intel", "compal", "asustek", "macbook"]
    yazicilar = ["epson", "canon", "brother", "ricoh", "lexmark", "hp printing", "xerox"]
    ag_cihazlari = ["tplink", "tp-link", "cisco", "zyxel", "netgear", "mikrotik", "ubiquiti", "huawei tech", "bilian", "zte", "shenzhen"]

    for marka in telefonlar:
        if marka in vendor:
            return "Telefon/Tablet"
    for marka in bilgisayarlar:
        if marka in vendor:
            return "Bilgisayar"
    for marka in yazicilar:
        if marka in vendor:
            return "Yazıcı"
    for marka in ag_cihazlari:
        if marka in vendor:
            return "Ağ Cihazı"

    return "Bilinmiyor"

def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        subprocess.run(
            ["ping", param, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2,
            check=True
        )
        return "Çevrimiçi"
    except subprocess.CalledProcessError:
        return "Cevap Yok"
    except subprocess.TimeoutExpired:
        return "Zaman Aşımı"

def port_tara(ip, portlar=[80, 443, 22, 3389]):
    aciklar = []
    for port in portlar:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                sonuc = s.connect_ex((ip, port))
                if sonuc == 0:
                    aciklar.append(str(port))
        except:
            pass
    return ", ".join(aciklar) if aciklar else "Yok"

def ag_tarama(ip_araligi="192.168.1.0/24"):
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ip_araligi)
    paket = ether / arp
    cevaplar, _ = srp(paket, timeout=2, verbose=False)

    cihazlar = []
    for _, cevap in enumerate(cevaplar):
        ip = cevap[1].psrc
        mac = cevap[1].hwsrc
        vendor = get_vendor(mac)
        tur = tahmin_et(vendor)
        durum = ping_ip(ip)
        acik_portlar = port_tara(ip)
        cihazlar.append((ip, mac, vendor, tur, durum, acik_portlar))
        progressbar.set(len(cihazlar) / len(cevaplar))
        app.update_idletasks()
    return cihazlar

def tara_ve_listele():
    tree.delete(*tree.get_children())
    ip_araligi = giris.get()
    progressbar.set(0)
    cihazlar = ag_tarama(ip_araligi)
    if not cihazlar:
        tree.insert("", "end", values=("Cihaz bulunamadı", "", "", "", "", ""))
    else:
        for cihaz in cihazlar:
            tree.insert("", "end", values=cihaz)
    progressbar.set(1)

# Arayüz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Ağ Tarayıcı v3")
app.geometry("1200x600")

giris = ctk.CTkEntry(app, placeholder_text="IP Aralığı (örn: 192.168.1.0/24)")
giris.insert(0, "192.168.1.0/24")
giris.pack(pady=10)

buton = ctk.CTkButton(app, text="Ağı Tara", command=tara_ve_listele)
buton.pack(pady=10)

progressbar = ctk.CTkProgressBar(app)
progressbar.set(0)
progressbar.pack(pady=5)

frame = ctk.CTkFrame(app)
frame.pack(expand=True, fill="both", padx=10, pady=10)

tree = ttk.Treeview(frame, columns=("IP", "MAC", "Marka", "Cihaz Türü", "Durum", "Açık Portlar"), show="headings")
tree.heading("IP", text="IP Adresi")
tree.heading("MAC", text="MAC Adresi")
tree.heading("Marka", text="Marka / Vendor")
tree.heading("Cihaz Türü", text="Cihaz Türü")
tree.heading("Durum", text="Durum")
tree.heading("Açık Portlar", text="Açık Portlar")
tree.pack(expand=True, fill="both")

app.mainloop()
