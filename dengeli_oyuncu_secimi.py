import random

# First, we create a list of players
footballers = [
    {"name": "Ahmet", "ability": 7},
    {"name": "Mehmet", "ability": 8},
    {"name": "Fatma", "ability": 3},
    {"name": "Ali", "ability": 9},
    {"name": "Ayşe", "ability": 4},
    {"name": "Elif", "ability": 3},
    {"name": "Emre", "ability": 8},
    {"name": "Gizem", "ability": 1},
    {"name": "Can", "ability": 6},
    {"name": "Deniz", "ability": 7},
    {"name": "Burak", "ability": 8},
    {"name": "Dilara", "ability": 6},
    {"name": "Ege", "ability": 7},
    {"name": "Esra", "ability": 4},
    {"name": "Furkan", "ability": 9},
    {"name": "Gökhan", "ability": 8},
    {"name": "İpek", "ability": 3},
    {"name": "İrem", "ability": 1},
    {"name": "İsmail", "ability": 7},
    {"name": "Kerem", "ability": 8},
    {"name": "Leyla", "ability": 2},
    {"name": "Mustafa", "ability": 7},
    {"name": "Nur", "ability": 3},
    {"name": "Özge", "ability": 4},
    {"name": "Pelin", "ability": 3},
    {"name": "Rümeysa", "ability": 2},
    {"name": "Sena", "ability": 1},
    {"name": "Tugba", "ability": 3},
    {"name": "Umut", "ability": 8},
    {"name": "Vildan", "ability": 2},
    {"name": "Yasemin", "ability": 5},
    {"name": "Zeynep", "ability": 2}
]

# We will randomly generate two teams using this list

while True:
    team_a = []
    team_b = []
    # We randomly select 14 of the football players    
    selected_footballers = random.sample(footballers, 14)
    

    # We loop to create the two teams
    for i, footballer in enumerate(selected_footballers):
        if i < 7:
            team_a.append(footballer)
        else:
            team_b.append(footballer)
    x=0
    y=0        
    for j in range(len(team_a)):
               
        x += team_a[j]["ability"]
        y += team_b[j]["ability"]
    
    if abs(x-y)<=1:
        break



# We print two player teams

print("Two teams have been created! first team: ")
for footballer in team_a:
    print(f"{footballer['name']} ({footballer['ability']})")
print("\nsecond team: ")
for footballer in team_b:
    print(f"{footballer['name']} ({footballer['ability']})")
    
    