import numpy as np
import torch.nn as nn
from .identity import Identity
from .jpeg_compression import JpegCompression
from .quantization import Quantization


class Noiser(nn.Module):
    """
    This module allows to combine different noise layers into a sequential noise module. The
    configuration and the sequence of the noise layers is controlled by the noise_config parameter.
    """
    def __init__(self, noise_type):
        super(Noiser, self).__init__()

        self.noise_layers = nn.ModuleList()
        self.noise_layers.append(Identity())
        
        if noise_type == 'no_noise':
            pass
        elif noise_type == 'combined':
            self.noise_layers.append(Crop((0.4, 0.55),(0.4, 0.55)))
            self.noise_layers.append(Cropout((0.25, 0.35),(0.25, 0.35)))
            self.noise_layers.append(Dropout(0.25, 0.03))
            self.noise_layers.append(Resize(0.4, 0.6))
            self.noise_layers.append(JpegCompression())
        else:
            raise NotImplementedError             

    def forward(self, encoded_and_cover):
        random_noise_layer = np.random.choice(self.noise_layers, 1)[0]
        return random_noise_layer(encoded_and_cover)
