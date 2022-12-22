import random

# Öncelikle, futbolculardan oluşan bir liste oluşturuyoruz
oyuncular = [
    {"name": "Ahmet", "yetenek": 7},
    {"name": "Mehmet", "yetenek": 8},
    {"name": "Fatma", "yetenek": 3},
    {"name": "Ali", "yetenek": 9},
    {"name": "Ayşe", "yetenek": 4},
    {"name": "Elif", "yetenek": 3},
    {"name": "Emre", "yetenek": 8},
    {"name": "Gizem", "yetenek": 1},
    {"name": "Can", "yetenek": 6},
    {"name": "Deniz", "yetenek": 7},
    {"name": "Burak", "yetenek": 8},
    {"name": "Dilara", "yetenek": 6},
    {"name": "Ege", "yetenek": 7},
    {"name": "Esra", "yetenek": 4},
    {"name": "Furkan", "yetenek": 9},
    {"name": "Gökhan", "yetenek": 8},
    {"name": "Hakan", "yetenek": 10},
    {"name": "İrem", "yetenek": 1},
    {"name": "İsmail", "yetenek": 7},
    {"name": "Kerem", "yetenek": 8},
    {"name": "Leyla", "yetenek": 2},
    {"name": "Mustafa", "yetenek": 7},
    {"name": "Nur", "yetenek": 3},
    {"name": "Özge", "yetenek": 4},
    {"name": "Pelin", "yetenek": 3},
    {"name": "Rümeysa", "yetenek": 2},
    {"name": "Sena", "yetenek": 1},
    {"name": "Tugba", "yetenek": 3},
    {"name": "Umut", "yetenek": 8},
    {"name": "takoz_recep", "yetenek": 2},
    {"name": "Yasemin", "yetenek": 5},
    {"name": "Zeynep", "yetenek": 2}
]

# Bu listeyi kullanarak rastgele iki takım oluşturacağız


while True:
    team_a = []
    team_b = []
    # Futbolculardan rastgele 14 tane seçiyoruz
    secilen_oyuncular = random.sample(oyuncular, 14)
    
    # Yeteneklerine göre sıralıyoruz
    #sorted_oyuncular = sorted(secilen_oyuncular, key=lambda x: x["yetenek"], reverse=True)

    # İki takımı oluşturmak için döngü oluşturuyoruz
    for i, oyuncu in enumerate(secilen_oyuncular):
        if i < 7:
            team_a.append(oyuncu)
        else:
            team_b.append(oyuncu)
    x=0
    y=0        
    for j in range(len(team_a)):
               
        x += team_a[j]["yetenek"]
        y += team_b[j]["yetenek"]
    
    if abs(x-y)<=1:
        break



# İki takımı yazdırıyoruz
print("İki takım oluşturuldu! İlk takım: ")
for oyuncu in team_a:
    print(f"{oyuncu['name']} ({oyuncu['yetenek']})")
print("\nİkinci takım: ")
for oyuncu in team_b:
    print(f"{oyuncu['name']} ({oyuncu['yetenek']})")