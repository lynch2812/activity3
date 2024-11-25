class player:
    def __init__(self, name, position, available =True):
        self.name = name
        self.position= position
        self.available = available

class squad:
    def __init__(self):
        self.players = []
    # adds a player to the squad (an instance)
    def add_player(self, player):
        self.players.append(player)

    # finds all the names matching the given name in the squad in uppercase using Lambda
    def search_by_name(self, name):
        search_name = lambda player: player.name.upper() == name.upper()
        return list(filter(search_name, self.players))
    

    # finds all the players  matching the given name using Lambda 
    def search_by_position(self, position):

        if isinstance(position, str):
            position = [position]
        
        search_position = lambda player: player.position.upper() in [pos.upper() for pos in position]
        return list(filter(search_position, self.players))
    
    # updates the availability  of a player by their name using Lambda
    def update_availability(self, name, available):
       
        update_player = lambda player: setattr(player, 'available', available) if player.name.upper() == name.upper() else None
        list(map(update_player, self.players))

    def list_available_players(self):
        return [player for player in self.players if player.available]

# Create instances of the player class, these are the players available to pick from
player1 = player("Courtouis", "gk")
player2 = player("ramos", "cb")
player3 = player("james ", "rb/cb")
player4 = player("cole","lb")
player5 = player("terry","cb")
player6 = player("figo","rm")
player7 = player("zidane", "acm")

# Create an instance of the Library class
squad = squad()

# Add players to the squad class above
squad.add_player(player1)
squad.add_player(player2)
squad.add_player(player3)
squad.add_player(player4)
squad.add_player(player5)
squad.add_player(player6)
squad.add_player(player7)

# Search for players by name
print("players available for the squad: ")
for player in squad.search_by_name("terry"):
 
    print(f"- {player.name} by {player.position}") 

# Search for players by position- change the position to search 

print("\nplayers in position :")
for player in squad.search_by_position(["cam", "gk"]):
    print(f"- {player.name} in {player.position}")

# Update player availability
squad.update_availability("", False)


# Check updated availability
print("\nAvailability of player:")
for player in squad.search_by_name(""):
    print(f"- {player.name} is {'available' if player.available else 'not fit for the squad'}")

# prints only the available players 
print("Available players for matchday")
for player in squad.list_available_players():
    print(f"-{player.name} plays in {player.position}")
