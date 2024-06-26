
__all__ = ['is_cat','learn','classify_image','categories','image','label','examples','intf']

# Cell
from fastai.vision.all import *
import gradio as gr


def is_cat(x): return x[0].isupper()

# Cell
learn = load_learner('model.pkl')

# Cell
categories = ('Dog', 'Cat')

def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

# Cell
image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)