# -*- coding: utf-8 -*-
"""flopcount.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R5PkmPB5W-M9u_gjl1NAsIpKn4pgMtAJ
"""

pip install fvcore

import torch
import torchvision.models as models
from transformers import BertModel
from fvcore.nn import FlopCountAnalysis, flop_count_table, flop_count_str

def analyze_model_flops(model, input_tensor, model_name):
    flops = FlopCountAnalysis(model, input_tensor)

    print(f"Total FLOPs for {model_name}: {flops.total()}")

    print(f"FLOPs by operator for {model_name}: {flops.by_operator()}")

    print(f"FLOPs by module for {model_name}: {flops.by_module()}")

    print(f"FLOPs by module and operator for {model_name}: {flops.by_module_and_operator()}")

    print(flop_count_table(flops))

    print(flop_count_str(flops))

dummy_input_cnn = torch.randn(1, 3, 224, 224)
dummy_input_bert = torch.randint(0, 30522, (1, 128))

vgg16_model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
vgg16_model.classifier[6] = torch.nn.Linear(in_features=4096, out_features=4)
analyze_model_flops(vgg16_model, dummy_input_cnn, "VGG16")

resnet50_model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
resnet50_model.fc = torch.nn.Linear(in_features=2048, out_features=4)
analyze_model_flops(resnet50_model, dummy_input_cnn, "ResNet50")

densenet121_model = models.densenet121(weights=models.DenseNet121_Weights.IMAGENET1K_V1)
densenet121_model.classifier = torch.nn.Linear(in_features=1024, out_features=4)
analyze_model_flops(densenet121_model, dummy_input_cnn, "DenseNet121")

bert_model = BertModel.from_pretrained("bert-base-uncased")
analyze_model_flops(bert_model, dummy_input_bert, "BERT-uncased")