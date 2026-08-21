import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/JPEG_example_flower.jpg/500px-JPEG_example_flower.jpg"
image_path = "/content/sample_data/sample.jpeg"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(image_path, 'wb') as out_file:
    out_file.write(response.read())


I = mpimg.imread(image_path)
H = I.shape[0] # number of rows -> height
W = I.shape[1] # number of columns -> width

print("Height is:", H)
print("Width is:", W)
