class MP3:
    def PlayMusic_Loop(filename : str):
        import ctypes
        winmm_lib = ctypes.cdll.LoadLibrary("Winmm")
        winmm_lib.mciSendStringW(bytes("play {}.mp3 repeat", "utf-8"), 0, 0, 0)
    def PlayMusic(filename : str):
        import ctypes
        winmm_lib = ctypes.cdll.LoadLibrary("Winmm")
        winmm_lib.mciSendStringW(bytes("play {}.mp3", "utf-8"), 0, 0, 0)
    def StopMusic(filename : str):
        import ctypes
        winmm_lib = ctypes.cdll.LoadLibrary("Winmm")
        winmm_lib.mciSendStringW(bytes("stop {}.mp3", "utf-8"), 0, 0, 0)