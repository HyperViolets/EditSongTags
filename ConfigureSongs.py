# parse through a CSV file
import csv
import eyed3
import os

# had to use easytag to add a title to every song
# no special symbols in csv
# clone from git then add file to source (Setting -> Project Structure -> Source)
# reinstall eyeD3 on computer
# set python interpreter to computer Python3
# before doing the actual process, test script on a clone folder of songs for any issues

songs_path = '/home/juan/Videos'


def edit_song_list():
    for (dir_path, dir_name, file_name) in os.walk(songs_path):
        for fn in file_name:
            matching_row = find_matching_details(fn)
            edit_song_tags(os.path.join(dir_path, fn), matching_row)
            rename_file(os.path.join(dir_path, fn), os.path.join(dir_path, matching_row[1]))


def rename_file(original_name, new_name):
    name_split = original_name.split('.')
    extention = new_name + '.' + name_split[len(name_split) - 1]
    os.rename(original_name, extention)

# change file[0] so that it can accept double digits (spaces and no space (just the number Ex. 2.mp3))


def find_matching_details(file):
    with open('/home/juan/Documents/SongListTest.csv') as csv_file:
        name_split = file.split(' ')[0]
        spam_reader = csv.reader(csv_file, delimiter=',')
        for row in spam_reader:
            if row[0] == name_split:
                return row


def edit_song_tags(file, row):
    audio_file = eyed3.load(file)

    # row[0] = Q
    # row[1] = Title
    # row[2] = Artist
    # row[3] = Album Artist
    # row[4] = Album
    # row[5] = Genre
    # row[6] = Comment
    # row[7] = Composer
    # row[8] = URL
    # row[9] = Bitrate
    # row[10] = Sample Rate
    # row[11] = Mode
    # row[12] = Size
    # row[13] = Duration
    # row[14] = Image
    # row[15] = Image Extention

    audio_file.tag.title = row[1]
    audio_file.tag.artist = row[2]
    audio_file.tag.album_artist = row[3]
    audio_file.tag.album = row[4]
    audio_file.tag.disc_num = None
    audio_file.tag.track_num = None
    audio_file.tag.genre = row[5]
    audio_file.tag.comments.set(u'' + row[6])
    audio_file.tag.composer = row[7]

    for my_section in audio_file.tag.user_url_frames:
        my_section.url = b''

    image_date = open(row[14], 'rb').read()
    audio_file.tag.images.set(3, image_date, row[15])
    audio_file.tag.save()


edit_song_list()
