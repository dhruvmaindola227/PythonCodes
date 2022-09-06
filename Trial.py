from pynput.keyboard import Key, Listener
import pafy
import vlc


def play_YT_music(url):

    # creating pafy object of the video
    video = pafy.new(url)

    # getting best stream
    best = video.getbestaudio()

    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)

    # start playing video
    media.play()


def show(key):

    print('\nYou Entered {0}'.format(key))

    if key == Key.delete:
        # Stop listener
        return False    

    if key.char == '1':
        play_YT_music("https://www.youtube.com/watch?v=L5GTkos3A-4")

    elif key.char == '2':
        play_YT_music("https://www.youtube.com/watch?v=SGPrOEZJPTQ&ab_channel=GameBugKnight")

    elif key.char == '3':
        play_YT_music("https://www.youtube.com/watch?v=ekL881PJMjI&list=PLya__OBTLMkPXKnf8MpK4SEpY1vrGWP2H&index=3&ab_channel=GamingSoundFX")


# Collect all event until released
with Listener(on_press = show) as listener:
    listener.join()