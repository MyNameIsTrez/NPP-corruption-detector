# NPP-corruption-detector

## libTAS for N++ setup

1. Download the latest version of libTAS [here](https://ci.appveyor.com/project/clementgallet/libtas/build/artifacts), and install it
2. If you now open a new terminal and type `libTAS`, it should open. You can also open libTAS with Ubuntu's "Activity overview" by pressing the Windows key, and then typing `libTAS`.
3. At the top of the `libTAS` window is a field called `Game executable`. You'll fill this by pressing the `Browse` button to the right of it. Find the `N++.bin.x86_64` on your computer. In my case its path was `/home/<user>/snap/steam/common/.local/share/Steam/steamapps/common/N++/N++.bin.x86_64`, but it is also likely to be `/home/<user>/.steam/steam/steamapps/common/N++/N++.bin.x86_64`.

There are some libTAS settings that need to be changed for N++ to run.
At the top of the libTAS window is a `Settings` button. Click that, and then click `Runtime`. 4. Under the `General` header, check the `Virtual Steam client` box. 5. At the top of the Settings page is a submenu called `Audio`. Go there, and under the `Audio Control` header, check the `Disable` box. You can now close the settings menu.

6. Press the `Start` button, and N++ should open, but be paused. You can unpause it at any time by keeping the libTAS window next to it, and pressing the `Pause` checkbox that's found at the bottom-left corner of the screen.

In order to record a movie, you'll want to press the `Stop` button in libTAS (or close the game), and press the `Movie recording` checkbox that's found below the `Game executable` text. You can then toggle between the `Recording` and `Playback` options in it.

TIP:
If you want the game to run at a higher framerate, outside of libTAS go to N++ its Options menu, then Graphics Options, and set the resolution way lower, and turn Fullscreen off.
My PC needs to have the resolution all the way down to 1280x720 in order to run at a consistent 60 FPS.

## Replaying the recording in an infinite loop using libTAS

Open a new terminal (Ctrl+Alt+T on Ubuntu), change `NPP_PATH` its value in the below command so it points to where you've installed N++, and run it:

```bash
NPP_PATH=~/snap/steam/common/.local/share/Steam/steamapps/common/N++
while true; do
    libTAS --non-interactive --read $NPP_PATH/N++.bin.x86_64.ltm $NPP_PATH/N++.bin.x86_64
    ./main.py
done
```

Here is what it looks like for me:

https://github.com/user-attachments/assets/80b9f3c3-b5b9-40c9-af84-e429318a7081

## Credits

- The main developer of libTAS, Kilaye/[Clément Gallet](https://github.com/clementgallet), for fixing a bug in libTAS for me that prevented N++ from running
- The Discord member Eddy/eddymatagallos, for having created and giving me a file that documents what all of the save file's bytes stand for
