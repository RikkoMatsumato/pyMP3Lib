def PlayMusic_Loop(filename):
    import ctypes
    winmm_lib = ctypes.WinDLL("Winmm.dll")
    winmm_lib.mciSendStringA(bytes("play {}.mp3 repeat".format(filename), "utf-8"), 0, 0, 0)
def PlayMusic(filename):
    import ctypes
    winmm_lib = ctypes.WinDLL("Winmm.dll")
    winmm_lib.mciSendStringA(bytes("play {}.mp3".format(filename), "utf-8"), 0, 0, 0)
def StopMusic(filename):
    import ctypes
    winmm_lib = ctypes.WinDLL("Winmm.dll")
    winmm_lib.mciSendStringA(bytes("stop {}.mp3".format(filename), "utf-8"), 0, 0, 0)
