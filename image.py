from PIL import Image, ImageOps

def load_image(filepath): return Image.open(filepath) 


def get_image_dimensions(image): return image.size

def get_pixel_layer(image): return image.load()

def resize_image(image, newX, newY): return ImageOps.contain(image, (int(newX), int(newY)))


