from PIL import Image, ImageOps
from colors import ColorMap
class StitchImage: 
    colorMap = ColorMap()
    simpleColorMap = colorMap.get_simple_map()

    def __init__ (self, filepath):
        self.originalImage = Image.open(filepath)
        self.currentImage = self.originalImage
        self.originalfilepath = filepath
        self.pixel_layer = self.originalImage.load()
        self.originalWidth = self.originalImage.size[0]
        self.originalHeight = self.originalImage.size[1]
        

    def load_image(filepath): return Image.open(filepath) 

    #returns image dimensions of the originally provided image in format [width, height]
    def get_original_image_dimensions(self): return self.originalImage.size

    #returns image dimensions of the current state of the image in format [width, height]
    def get_current_image_dimension(self): return self.currentImage.size

    def get_pixel_layer(self): return self.originalImage.load()

    #"Returns a resized version of the image, set to the maximum width and height within the requested size, while maintaining the original aspect ratio."
    # https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.contain
    def resize_image(self,newX, newY): 
        print(f"Resizing image to: {newX}, {newY}")
        self.currentImage = ImageOps.contain(self.originalImage, (int(newX), int(newY)))
        return self.currentImage

    # walks through each pixel in the current image and maps it to the closest color in the color map 
    def map_pixels(self): 
        # print(f"pixel {self.pixel_layer[100,2]}")
        width, height = self.get_current_image_dimension()
        dummy_count = 0 #does nothing, just for testing
        print(f"width and height are: {width} and {height}")
        for h in range(self.originalHeight): 
            for w in range(self.originalWidth): 
                #do color map things 
                dummy_count += 1 #does nothing, just for testing
        # print(f"Color map is accessible: {self.simpleColorMap}")

    #saves the current state of the image
    def save_image(self,filepath): return self.currentImage.save(filepath)
