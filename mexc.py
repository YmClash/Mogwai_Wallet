import gradio as gr

def greet(name):
  return "Bonjour " + name + " !"

description = '<h1 style="font-size:70px;">AJUNA WALLET CHECKER </h1>'

iface = gr.Interface(fn=greet, inputs="text", outputs="text", description=description)
iface.launch()