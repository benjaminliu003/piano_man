# ideas:
# - maybe use avail libs to break down files and rep as an image to process, we can scrape most data with existing libs
# - then use that func to feed to a machine to do model training?
# - REMEMBER TO FIND OUT HOW TO EXPORT A CREATED MODEL

import os
import librosa as au  # maybe we can use gpu accel-ed package in the future.
from librosa import display as disp
import matplotlib.pyplot as pl  # This is just to make sure we can get a graph, debug use


class PreProcessed:

    def loadnview(self, loadpath):
        sample = au.get_samplerate(loadpath)
        # we gotta try this with a supported audio type - try converting to a SoundFile supported codec
        # Then feed to function
        loaded = au.load(loadpath, sr=sample, mono=True)
        # audio becomes float 32 but not a numpy float 32 array, weird

        # call a member function to process signal here - we skip here to check we can see data

        disp.waveshow(loaded, sr=sample)
        print(loaded)  # dev print line


inputpath = input('Input audio path: ')  # note to self: get rid of quotation marks when entering path
viewTest = PreProcessed()
viewTest.loadnview(inputpath)

# input test file - C:\Users\Ben\Downloads\Car.mp3
# current output - (array([], dtype=float32), 48000)
