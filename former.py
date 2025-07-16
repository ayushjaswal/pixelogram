from PIL import Image
import os
import numpy as np
from fetcher import Fetcher


class Former():
    def __init__(self, style):
        self.style = style


    def pixelate_image(self,image_path, pixel_factor_size=4, threshold=188):

        """ This function downsize (pixelate) the loaded image
            It works this by encompassing the 

        """
        fetcher = Fetcher()
        fetcher.fetch_image(image_path=image_path)
        value = fetcher.image_value()
        img = fetcher.image()
        
        downsize = img.resize(
            (img.width // pixel_factor_size, img.height // pixel_factor_size),
        )
        bw_small = downsize.point(lambda p: 255 if p > threshold else 0)
        bw_pixelated = bw_small.resize(img.size, Image.NEAREST)
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", image_path + "_output.png") 

        if path:
            bw_pixelated.save(path)
        else:
            bw_pixelated.show()

        return bw_pixelated

if __name__ == "__main__":
    image_path = input("Image path: ")
    style_ = input("Select style: \n1. Pixelated\n2. Terminal")


    former = Former(style=style_)
    former.pixelate_image(image_path=image_path)
     


        
