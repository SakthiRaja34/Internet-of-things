import vlc
import time

player = vlc.MediaPlayer("audio.song.mp3")
player.play()
time.sleep(15)