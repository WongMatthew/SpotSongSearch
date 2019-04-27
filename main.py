# Open file
file = open('spotify.csv')
file.readline()

# ----------- Search through file ----------- #

# Initialize a song
drake_songs = []
artist_o_songs = []

# Go through each line in the file
for line in file:

  # Separate the string at commas and cast values to their appropriate types
  song = line.strip().split(',')
  artist = str(song[-1])
  song_title = str(song[-2])
  danceability = float(song[2])

  # Add to the Drake songs list if its a Drake song
  if artist == "Drake":
    drake_songs.append([danceability, song_title, artist])
  # If the first character in the artist is 'O' store the artist
  if artist[0] == 'O':
    artist_o_songs.append([song_title, artist])
# TEST
print("Dance Score \t\tSong")

for song in drake_songs:
  print(str(song[0]) + "\t\t\t\t" + song[1])

print("-------------------------")
print("All songs that have artists that start with 'O'")
for song in artist_o_songs:
  print(song[1] + "\t\t\t\t\t\t\t\t\t\t by " + song[0])