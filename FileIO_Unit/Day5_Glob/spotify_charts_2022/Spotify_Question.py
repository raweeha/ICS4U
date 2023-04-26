## #{ #SongName by Artist: {date: # streams, date: #streams, etc }, 
##   #SongName by Artist: {date: # streams, date: #streams, etc } , . . .    etc.}
##
import glob, csv

song_dict = {}

all_file_pointers = glob.glob('regional-global-data-*.csv')

for filename in all_file_pointers:

    with open(filename, encoding = 'utf-8', errors = 'ignore') as file_in:

        reader = csv.DictReader(file_in)

        date = filename[22:32]

        for line in reader:

            keys = f'{line["track_name"]} by {line["artist_names"]}'

            if keys not in song_dict:

                song_dict[keys] = {}

            song_dict[keys][date] = line["streams"]

print(song_dict)
                

##import glob, csv
##
##all_csv_files = glob.glob("*.csv")
##
##streamed_songs_dict = {}
##for csv_file in all_csv_files:
##
##    with open(csv_file, encoding="utf-8") as file_stream:
##        all_dict_songs  = csv.DictReader(file_stream)
##        date = csv_file[22:32]
##
##        for song in all_dict_songs:
##            key_name = f'{song["track_name"]} by {song["artist_names"]}'
##            
##            if key_name not in streamed_songs_dict:
##                streamed_songs_dict[key_name] = {}
##
##            streamed_songs_dict[key_name][date] = song["streams"]
##
##print(streamed_songs_dict)
