import gradio as gr

def greet(name):
  return "Bonjour " + name + " !"

description = '<h1 style="font-size:15px;">Mon titre</h1>'

iface = gr.Interface(fn=greet, inputs="text", outputs="text", description=description)
iface.launch()