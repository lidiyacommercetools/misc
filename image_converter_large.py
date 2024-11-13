from PIL import Image
import os, glob

directory = '/Users/lidiyadzhumayeva/Desktop/goodstore_images'
files = os.listdir(directory)
index = 0
while index < len(files):
    filename = files[index]
    if filename.endswith('.jpeg'):
        with open(os.path.join(directory, filename)) as f:
            image = Image.open(filename)
            image.thumbnail((700,700))
            image.save("updated_images/" + str(filename)[:-5] + "-large.jpeg", "jpeg")
    index += 1
