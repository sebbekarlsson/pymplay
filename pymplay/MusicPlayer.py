from subprocess import Popen, PIPE
import os.path
import time


class MusicPlayer(object):

    def __init__(self):
        self.playlist = []


    def play_audio(self, filename):
        if not os.path.isfile(filename):
            raise Exception('NoSuchFile')

        shell = Popen(['play', filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output = shell.returncode
        time.sleep(3)
        while output is not None:
            pass

        return True


    def add_audio(self, filename):
        if not os.path.isfile(filename):
            raise Exception('NoSuchFile')

        self.playlist.append(filename)


    def play_playlist(self):
        for audio in self.playlist:
            if not os.path.isfile(audio):
                raise Exception('NoSuchFile')
                
            self.play_audio(audio)