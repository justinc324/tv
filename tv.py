import cv2
import numpy as np
import pygame as pg
from pathlib import Path
import keyboard
from omxplayer.player import OMXPlayer

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN)

# global variables
DELAY = 2
VID_COUNT = 3
MUSIC_COUNT = 4
AUDIO_COUNT = 2
VID_ITER = 0
MUSIC_ITER = 0
AUDIO_ITER = 0

# intialize
# pg.mixer.init()
# pg.init()
# pg.mixer.set_num_channels(12)
#
# mixer = pg.mixer
# channel0 = mixer.Channel(0)
# channel1 = mixer.Channel(1)

# music to play
# office_theme = mixer.Sound("music/office_theme_song.wav")
# agni_kai = mixer.Sound("music/last_agni_kai.wav")
# succession_theme = mixer.Sound("music/succession_theme.wav")

# music to play
office_theme = OMXPlayer(Path('music/office_theme_song.wav'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer4', args='--loop')
office_theme.pause()
agni_kai = OMXPlayer(Path('music/last_agni_kai.wav'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer5', args='--loop')
agni_kai.pause()
succession_theme = OMXPlayer(Path('music/succession_theme.wav'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer6', args='--loop')
succession_theme.pause()
fun_song = OMXPlayer(Path('music/fun_song.wav'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer7', args='--loop')
fun_song.pause()

music = (office_theme, agni_kai, succession_theme, fun_song)


# audio files

# dwight_fire_drill = mixer.Sound("audio/dwight_fire_drill.wav")
# kendall_succession = mixer.Sound("audio/kendall_succession.wav")

audio = (dwight_fire_drill, kendall_succession)

# visuals
# video_agni_kai = cv2.VideoCapture('video/agnikai.mp4')
# video_fire_drill = cv2.VideoCapture('video/fire_drill.mp4')
# video_kendall_succession = cv2.VideoCapture('video/kendall_succession.mp4')

# visuals
video_agni_kai = OMXPlayer(Path('video/agnikai.mp4'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer1', args='--loop')
video_agni_kai.pause()
video_fire_drill = OMXPlayer(Path('video/fire_drill.mp4'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer2', args='--loop')
video_fire_drill.pause()
video_kendall_succession = OMXPlayer(Path('video/kendall_succession.mp4'),
        dbus_name='org.mpris.MediaPlayer2.omxplayer3', args='--loop')
video_kendall_succession.pause()

videos = (video_agni_kai, video_fire_drill, video_kendall_succession)




curr_player = video_agni_kai
curr_player.play()

# current audio
muted = False

while True:

    switch = GPIO.input(3)

    if keyboard.is_pressed('a'):
        curr_player.pause()
        VID_ITER = (VID_ITER + 1) % VID_COUNT
        curr_player = videos[VID_ITER]
        curr_player.play()

    # mute/unmute audio from original clip
    if keyboard.is_pressed('m'):
        if muted:
            curr_player.unmute()
            muted = False
        else:
            curr_player.mute()
            muted = True

    # play music
    if keyboard.is_pressed('z'):
    # if GPIO.input(3) is not switch:
        music[MUSIC_ITER].pause()
        MUSIC_ITER = (MUSIC_ITER + 1) % MUSIC_COUNT
        music[MUSIC_ITER].play()
        # channel0.play(music[MUSIC_ITER], -1)
        switch = not(switch)


    # play an alternate audio file. Mutes the current audio.
    if keyboard.is_pressed('w'):
        AUDIO_ITER = (AUDIO_ITER + 1) % AUDIO_COUNT
        curr_player.mute()
        muted = True
        # mixer.Channel(1).play(audio[AUDIO_ITER])


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
# cap = video_agni_kai
# window_name = "window"
#
# # Check if camera opened successfully
# if (cap.isOpened()== False):
#   print("Error opening video stream or file")
#
# # Read until video is completed
#
# # Full screen on the video
# cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#
# channel0.play(office_theme, -1)
# while(cap.isOpened()):
#   # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:
#
#         # Display the resulting frame
#         cv2.imshow(window_name,frame)
#
#         # Press Q on keyboard to  exit
#
#         if cv2.waitKey(DELAY) & 0xFF == ord('q'):
#             break
#         elif cv2.waitKey(DELAY) & 0xFF == ord('a'):
#             VID_ITER = (VID_ITER + 1) % VID_COUNT
#             cap = videos[VID_ITER]
#             DELAY = delays[VID_ITER]
#         elif cv2.waitKey(DELAY) & 0xFF == ord('z'):
#             MUSIC_ITER = (MUSIC_ITER + 1) % MUSIC_COUNT
#             channel0.play(music[MUSIC_ITER], -1)
#         elif cv2.waitKey(DELAY) & 0xFF == ord('w'):
#             pass
#
#         # if cv2.waitKey(DELAY) & 0xFF == ord('q'):
#         #     break
#         # elif cv2.waitKey(DELAY) & 0xFF == ord('a'):
#         #     VID_ITER = (VID_ITER + 1) % VID_COUNT
#         #     cap = videos[VID_ITER]
#         #     DELAY = delays[VID_ITER]
#         # elif cv2.waitKey(DELAY) & 0xFF == ord('z'):
#         #     MUSIC_ITER = (MUSIC_ITER + 1) % MUSIC_COUNT
#         #     channel0.play(music[MUSIC_ITER], -1)
#         # elif cv2.waitKey(DELAY) & 0xFF == ord('w'):
#         #     pass
#
#
#   # Break the loop
#     else:
#         break
#
# # When everything done, release the video capture object
# cap.release()
#
# # Closes all the frames
# cv2.destroyAllWindows()
