from PIL import Image
import numpy as np


class Fetcher():
    def __init__(self):
        pass

    def fetch_image(self, image_path):
        self.image_path = image_path
        self.img = Image.open(image_path).convert("RGB")
        self.pixels = self.img.load()
        
    def image_value(self):
        if not self.pixels:
            raise ValueError("Image not fetched, please fetch the image first")
        return np.array(self.img)

    def image(self):
        return self.img

if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.fetch_image("./test.png")
    value = fetcher.image_value()
    print(value)
