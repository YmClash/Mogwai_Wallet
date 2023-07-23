import gradio


def hallo(name):
    return  f'Hello {name}'


interface =  gradio.Interface(fn=hallo,inputs="text", outputs="text")

interface.launch()