import argparse
import os

import image

# use this to test: python main.py sskaeeoh_tshirt.png 400 500 

def crossStitchParser(): 
    parser = argparse.ArgumentParser(description="Generate a cross stitch pattern from any image!")
    
    parser.add_argument('filepath', type=str, help='full file path to your image file')
    parser.add_argument('y', type=int, help='the number of desired pixels on the y axis')
    parser.add_argument('x', type=int, help = 'the number of desired pixels on the x axis')
    return parser

if __name__ == "__main__": 
    parser = crossStitchParser()
    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        raise Exception(f"Filepath {args.filepath} is not found")

    print(f"Generating a {args.x} x {args.y} crossstitch pattern for {args.filepath} ")
    
    original_image = image.load_image(args.filepath)
    resized_image = image.resize_image(original_image, args.x, args.y)
    pixel_layer = image.get_pixel_layer(resized_image)
    