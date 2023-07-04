import random

import numpy as np
import time
import gradio


def dom(number) :
    numb = random.randint(1, number)

    # list = [random.randint(1, 1000) for o in range(1, 10)]
    return numb


def binaire(numb) :
    numb = int(numb)
    numb = bin(numb)
    return numb


#la  classe gradio.Interface(fn, inputs, outputs)

test_room = gradio.Interface(dom, "number", "number")
#
#
#
test_room.launch()



# liste_address = ['5G6s3tvwCbQ7MZWYmUrZkG8iYxYwAG8usqM57yJF8bU8Dbvr',
                 # '5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY',
                 # '5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty',
                 # '5FLSigC9HGRKVhB9FiEo4Y3koPsNmBmLJbpXg2mp1hXcS59Y',
                 # '5DAAnrj7VHTznn2AWBemMuyBwZWs6FNFjdyVXUeYum3PTXFy',
                 # '5HGjWAeFDfFCWPsjFQdVV2Msvz2XtMktvgocEZcCj68kUMaw',
                 # '5CiPPseXPECbkjWCa6MnjNokrgYjMqmKndv2rSnekmSK2DjL',
#                ]

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
