import argparse
import cleanup
import os
from image import StitchImage
# use this to test: python main.py sskaeeoh_tshirt.png 400 500 

def crossStitchParser(): 
    parser = argparse.ArgumentParser(description="Generate a cross stitch pattern from any image!")
    
    parser.add_argument('filepath', type=str, help='full file path to your image file')
    parser.add_argument('newfilename', type=str, help='the new filename to save your resized file, saved under build/')
    parser.add_argument('y', type=int, help='the number of desired pixels on the y axis')
    parser.add_argument('x', type=int, help = 'the number of desired pixels on the x axis')
    parser.add_argument('--clean', type=bool, default = False, help='optional, default False, deletes previously generated images under build/')
    return parser



if __name__ == "__main__": 

    parser = crossStitchParser()
    args = parser.parse_args()

    if args.clean: 
        cleanup.cleanup()

    if not os.path.exists(args.filepath):
        raise Exception(f"Filepath {args.filepath} is not found")

    print(f"Generating a {args.x} x {args.y} crossstitch pattern for {args.filepath} ")
    
    myImage = StitchImage(args.filepath)
    myImage.resize_image(args.x, args.y)
    pixel_layer = myImage.get_pixel_layer()

    os.makedirs("build", exist_ok=True)
    
    outputfile = "build/" + args.newfilename
    
    myImage.save_image(outputfile)
