import gradio
import random

numb = [random.randint(1, 100) for i in range(1)]
print(numb)


def gen_number(number):
    numb = [random.randint(1, 100) for i in range(number)]
    return numb


def greet(name):
    return "HELLO" + name


# demo = gradio.Interface(fn=gen_number, inputs="number", outputs="text")
#
# demo.launch()

balance = 1234.56789012
decimal_precision = 8
formatted_balance = str(round(balance, decimal_precision))
print(formatted_balance)

