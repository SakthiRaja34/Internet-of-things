import vlc
import time


instance = vlc.Instance()
media_player = instance.media_player_new()
list_player = instance.media_list_player_new()
list_player.set_media_player(media_player)


playlist_files = ["audio1.mp3","audio.song.mp3"]

# Create MediaList and add Media objects
media_list = instance.media_list_new()
for file in playlist_files:
    media = instance.media_new(file)
    media_list.add_media(media)

list_player.set_media_list(media_list)

# Play playlist
list_player.play()

# Wait until playlist finishes
while True:
    state = list_player.get_state()
    if state == vlc.State.Ended or state == vlc.State.Error:
        break
    time.sleep(1)
