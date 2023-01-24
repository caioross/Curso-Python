from tqdm.notebook import trange
from IPython.display import Image, display
from deep_daze import Imagine

TEXT = 'a cat on watermelon' #@ param {type:"string"}
NUM_LAYERS = 32 #@ param {type:"number"}
SAVE_EVERY =  20#@ param {type:"number"}
IMAGE_WIDTH = 256 #@ param {type:"number"}
SAVE_PROGRESS = True #@ param {type:"boolean"}
LEARNING_RATE = 1e-5 #@ param {type:"number"}
ITERATIONS = 500 #@ param {type:"number"}

model = Imagine(
    text = TEXT,
    num_layers = NUM_LAYERS,
    save_every = SAVE_EVERY,
    image_width = IMAGE_WIDTH,
    lr = LEARNING_RATE,
    iterations = ITERATIONS,
    save_progress = SAVE_PROGRESS
)
for epoch in trange(20, desc = 'epochs'):
    for i in trange(ITERATIONS, desc = 'iteration'):
        model.train_step(epoch, i)
        if i % model.save_every != 0:
            continue
        filename = TEXT.replace(' ', '_')
        image = Image(f'./{filename}.jpg')
        #image = Image('./' + filename + '.jpg')
        display(image)
