from inception_resnet_v1 import InceptionResnetV1
from densenet import DenseNet
import torch
import torch.nn as nn
import requests
import os
from requests.adapters import HTTPAdapter


class FECNet(nn.Module):
    """FECNet model with optional loading of pretrained weights.
    Model parameters can be loaded based on pretraining on the Google facial expression comparison
    dataset (https://ai.google/tools/datasets/google-facial-expression/). Pretrained state_dicts are
    automatically downloaded on model instantiation if requested and cached in the torch cache.
    Subsequent instantiations use the cache rather than redownloading.
    Keyword Arguments:
        pretrained {str} -- load pretraining weights
    """
    def __init__(self, pretrained=False):
        super(FECNet, self).__init__()
        growth_rate = 64
        depth = 100
        block_config = [5]
        efficient = True
        #self.Inc = InceptionResnetV1(pretrained='vggface2', device='cuda').eval()
        self.Inc = InceptionResnetV1(pretrained='vggface2').eval()
        for param in self.Inc.parameters():
            param.requires_grad = False
        self.dense = DenseNet(growth_rate=growth_rate,
                        block_config=block_config,
                        num_classes=16,
                        small_inputs=True,
                        efficient=efficient,
                        num_init_features=512)

        if (pretrained):
            load_weights(self)

    def forward(self, x):
        feat = self.Inc(x)[1]
        out = self.dense(feat)
        return out