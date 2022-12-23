import random

# First, we create a list of players
players = [
    {"name": "james", "ability": 7},
    {"name": "Emily", "ability": 8},
    {"name": "Michael", "ability": 3},
    {"name": "Jessica", "ability": 9},
    {"name": "Matthew", "ability": 4},
    {"name": "Ashley", "ability": 3},
    {"name": "Christopher", "ability": 8},
    {"name": "Taylor", "ability": 1},
    {"name": "Daniel", "ability": 6},
    {"name": "Rachel", "ability": 7},
    {"name": "Ryan", "ability": 8},
    {"name": "Nicholas", "ability": 6},
    {"name": "Alexander", "ability": 7},
    {"name": "Megan", "ability": 4},
    {"name": "Samantha", "ability": 9},
    {"name": "William", "ability": 8},
    {"name": "David", "ability": 3},
    {"name": "Benjamin", "ability": 1},
    {"name": "Elizabeth", "ability": 7},
    {"name": "John", "ability": 8},
    {"name": "Robert", "ability": 2},
    {"name": "Joseph", "ability": 7},
    {"name": "Rebecca", "ability": 3},
    {"name": "Richard", "ability": 4},
    {"name": "Susan", "ability": 3},
    {"name": "Remy", "ability": 10},
    {"name": "Charles", "ability": 1},
    {"name": "Patricia", "ability": 3},
    {"name": "Thomas", "ability": 8},
    {"name": "Jennifer", "ability": 2},
    {"name": "Kevin", "ability": 5},
    {"name": "Melissa", "ability": 2}
]

# We will randomly generate two teams using this list

while True:
    team_a = []
    team_b = []
    # We randomly select 14 of the players    
    selected_players = random.sample(players, 14)
    

    # We loop to create the two teams
    for i, player in enumerate(selected_players):
        if i < 7:
            team_a.append(player)
        else:
            team_b.append(player)
    x=0
    y=0        
    for j in range(len(team_a)):
               
        x += team_a[j]["ability"]
        y += team_b[j]["ability"]
    
    if abs(x-y)<=1:
        break



# We print two player teams

print("Two teams have been created! first team: ")
for player in team_a:
    print(f"{player['name']} ({player['ability']})")
print("\nSecond team: ")
for player in team_b:
    print(f"{player['name']} ({player['ability']})")
    
    