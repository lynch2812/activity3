

scary = input("Is the movie scary?(yes/no): ").lower() == "yes" 
funny = input("Is the movie funny?(yes/no): ").lower() == "yes"
romantic = input("Is the movie romantic?(yes/no): ").lower() == "yes"
scifi = input("Is the movie about aliens?:(yes/no) ").lower() == "yes"

if scary and funny and not romantic and not scifi:
  genre = "Horrorcom"
elif funny and romantic and not scary and not scifi:
  genre = "Romcom"
elif romantic:
  genre =  "Romance"
elif funny:
  genre = "Comedy"
elif scifi:
  genre = "Sci-fi"
elif scary:
  genre = "Horror"
else:
  genre = "unknown"

if genre == "Horrorcom":
  print("This film is a Horrorcom")
elif genre == "Romcom":
  print("This film is a Romcom")
elif genre == "Romance":
  print("This film is a Romance")
elif genre == "Comedy":
  print("This is a Comedy")
elif genre == "Horror":
  print("This is a Horror")
elif genre == "Sci-fi":
  print("This film is a Sci-fi")
else:
  print("unknown genre")
  








 
