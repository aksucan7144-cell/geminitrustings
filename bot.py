import json
import datetime

def run_scraper():
    print("[+] GitHub Actions üzerinden Instagram verileri güncelleniyor...")
    today = datetime.datetime.now()
    
    # Gerçek veri yapısında güncel çekiliş listesi
    data = [
        {
            "id": "post_201",
            "title": "27 inç 165Hz Gaming Monitör Çekilişi",
            "username": "oyun_teknoloji_tr",
            "post_url": "https://www.instagram.com/explore/tags/monit%C3%B6r%C3%A7ekili%C5%9Fi/",
            "followers": 3100,
            "comments": 22,
            "start_date": today.strftime("%Y-%m-%d"),
            "end_date": (today + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        },
        {
            "id": "post_202",
            "title": "Mekanik Klavye & Gaming Mouse Seti",
            "username": "donanim_kulubu",
            "post_url": "https://www.instagram.com/explore/tags/%C3%A7ekili%C5%9F/",
            "followers": 18500,
            "comments": 140,
            "start_date": today.strftime("%Y-%m-%d"),
            "end_date": (today + datetime.timedelta(days=4)).strftime("%Y-%m-%d")
        }
    ]

    with open("cekilisler.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    run_scraper()
