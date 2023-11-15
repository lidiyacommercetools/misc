directory = '/Users/lidiyadzhumayeva/Desktop/goodstore_images'
files = os.listdir(directory)
index = 0
while index < len(files):
    filename = files[index]
    if filename.endswith('.jpeg'):
        with open(os.path.join(directory, filename)) as f:
            image = Image.open(filename)
            new_image = image.resize((700, 700))
            new_image.save("updated_images/" + str(filename)[:-5] + "-large.jpeg", "jpeg")
    index += 1
