from PIL import Image, ImageOps

class StitchImage: 
    def __init__ (self, filepath):
        self.originalimage = Image.open(filepath)
        self.currentImage = self.originalimage
        # self.originalX = self.originalimage.get_image_dimensions

    def load_image(filepath): return Image.open(filepath) 

    #returns image dimensions of the originally provided image
    def get_image_dimensions(self): return self.originalimage.size

    def get_pixel_layer(self): return self.originalimage.load()

    #"Returns a resized version of the image, set to the maximum width and height within the requested size, while maintaining the original aspect ratio."
    # https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.contain
    def resize_image(self,newX, newY): 
        print(f"Resizing image to: {newX}, {newY}")
        self.currentImage = ImageOps.contain(self.originalimage, (int(newX), int(newY)))
        return self.currentImage

    #saves the current state of the image
    def save_image(self,filepath): return self.currentImage.save(filepath)
