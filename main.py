import threading
from playsound import playsound
from threading import *

t2 = threading.Thread(target=playsound, args=('audio/He_able.mp3',),kwargs={'block':False})
t2.start()

t = threading.Thread(target=playsound, args=('audio/Orin.mp3',),kwargs={'block':False})
t.start()
playsound('audio/Orin.mp3',block=False)


