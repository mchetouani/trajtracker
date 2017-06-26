"""

TrajTracker - stimuli package

@author: Dror Dotan
@copyright: Copyright (c) 2017, Dror Dotan
"""

from enum import Enum
Orientation = Enum('Orientation', 'Horizontal Vertical')

#  Import the package classes
from ._BaseMultiStim import BaseMultiStim
from ._FixationZoom import FixationZoom
from ._NumberLine import NumberLine
from ._Slider import Slider
from ._StimulusContainer import StimulusContainer
from ._StimulusSelector import StimulusSelector
from ._MultiStimulus import MultiStimulus
from ._MultiTextBox import MultiTextBox
