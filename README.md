# realtime_eeg
Library for realtime EEG decoding from Backyard Brains Spikerbox.

Early development of platform for EEG-controlled drone. The basic idea is to use mental states (e.g. thinking about squeezing right hand, color red, etc) decoded from Backyard Brains EEG kit to input controls to drone.

## Scripts:

### byb.py
Pulled from Backyard Brains github (script by Stanislav Mircic). Allows for realtime streaming of data from Spikerbox into python.
 
### tonegenerator.py
Runs PsychoPy script which cycles through mental states each block. 
Every trial generates a tone which indicates the user should start thinking about the target state for that block.
