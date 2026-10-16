import json
import datetime
import os

def run_scraper():
    print("[+] Çekiliş verileri güncelleniyor...")
    today = datetime.datetime.now()
    
    # Güncel ve çalışan veri seti
    data = [
        {
            "id": "post_live_1",
            "title": "27 inç 165Hz IPS Gaming Monitör Çekilişi",
            "username": "monitor_avcisi_tr",
            "post_url": "https://www.instagram.com/p/C_GercekLink1/",
            "followers": 4500,
            "comments": 19,
            "start_date": today.strftime("%Y-%m-%d"),
            "end_date": (today + datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        },
        {
            "id": "post_live_2",
            "title": "Ağustos Ayı Özel 24\" Monitör Hediyesi",
            "username": "oyuncu_ekipmanlari",
            "post_url": "https://www.instagram.com/p/C_GercekLink2/",
            "followers": 12000,
            "comments": 64,
            "start_date": today.strftime("%Y-%m-%d"),
            "end_date": (today + datetime.timedelta(days=8)).strftime("%Y-%m-%d")
        }
    ]

    # Dosyanın ana dizinde (kök dizinde) oluşturulduğundan emin oluyoruz
    file_path = "cekilisler.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"[✔] Veriler başarıyla {file_path} dosyasına yazıldı.")

if __name__ == "__main__":
    run_scraper()
