# https://github.com/face-hh/0xbj/blob/main/Virus/src/wallpaper.py
import ctypes, sys, os

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(sys.argv[1]) , 0)
