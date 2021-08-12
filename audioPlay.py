import vlc


def playAudio(number,type):
    media = vlc.MediaPlayer("song"+type+number+".mp3")
    media.audio_set_volume(100)
    media.play()


if __name__ == "__main__":
    playAudio("1","KeyMsg")