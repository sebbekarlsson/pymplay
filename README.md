# PyMPlay
> Play audio with Python.<br>
> (This is sort of like a wrapper for 'sox')

## Example

    from pymplay.pymplay.MusicPlayer import MusicPlayer

    player = MusicPlayer()

    player.add_audio('fileout.flac')
    player.add_audio('applause.flac')

    player.play_playlist()

    player.play_audio('applause.flac')

## Install
> First run:
>
    sudo python3 setup.py install
>
> If you are on Arch Linux run:
>
    sudo bash install_arch.sh
>
> Otherwise, run:
>
    sudo bash install.sh