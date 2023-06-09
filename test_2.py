import random

import numpy as np
import time
import gradio


def dom(numb) :
    numb = random.randint(1, 1000)
    # list = [random.randint(1, 1000) for o in range(1, 10)]
    return numb


def binaire(numb) :
    numb = int(numb)
    numb = bin(numb)
    return numb


#gradio.Interface(fn, inputs, outputs)

test_room = gradio.Interface(binaire, "number", "text")
#
#
#
test_room.launch()

# #
# def binary(numb):
#     numb = int(numb)
#     numb = bin(numb)
#
#     return numb
#
# binary(5475785754545)
# #
# # numb = int(input('Entrez un nombre : '))
# # numb = bin(numb)
# # print(str(numb))
# # #
