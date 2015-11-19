from pymplay.MusicPlayer import MusicPlayer


def test():
    player = MusicPlayer()

    player.add_audio('pymplay/tests/stubbs/fileout.flac')
    player.add_audio('pymplay/tests/stubbs/applause.flac')

    player.play_playlist()