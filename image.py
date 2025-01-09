import numpy as np 
from PIL import Image, ImageOps
from colors import ColorMap
from scipy.spatial import cKDTree
class StitchImage: 
    colorMap = ColorMap()
    simpleColorMap = colorMap.get_simple_map()

    def __init__ (self, filepath):
        self.originalImage = Image.open(filepath)
        self.currentImage = self.originalImage
        self.originalfilepath = filepath
        self.original_pixel_layer = self.originalImage.load()
        self.current_pixel_layer = self.currentImage.load()
        self.originalWidth = self.originalImage.size[0]
        self.originalHeight = self.originalImage.size[1]
        self.currentWidth = self.currentImage.size[0]
        self.currentHeight = self.currentImage.size[1]

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
        self.current_pixel_layer = self.currentImage.load()
        self.currentWidth = self.currentImage.size[0]
        self.currentHeight = self.currentImage.size[1]
        return self.currentImage

    # walks through each pixel in the current image and maps it to the closest color in the color map 
    def map_pixels(self): 
        # print(f"pixel {self.pixel_layer[100,2]}")
        height, width = self.get_current_image_dimension()

        self.find_nearest_pixel(self.current_pixel_layer[0,0])
        result = []

        print(f"Size of current image is {self.currentWidth} x {self.currentHeight}")
        for h in range(self.currentHeight): 
            temp_row = []
            for w in range(self.currentWidth): 
                #do color map things 
                temp_row.append(self.find_nearest_pixel(self.current_pixel_layer[w,h]))
            result.append(temp_row)
        
        result = np.array(result, dtype=np.uint8)
        newImage = Image.fromarray(result)
        return newImage


    def find_nearest_pixel(self, pixel):

        result = cKDTree(self.simpleColorMap).query(pixel, k=1) # get the euclidean distance and then the index of the closest color (euclidean distance, index of closest color )

        nearest = self.simpleColorMap[result[1]]
        return nearest


    #saves the current state of the image
    def save_image(self,filepath): return self.currentImage.save(filepath)
