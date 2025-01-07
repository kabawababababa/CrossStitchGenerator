import argparse
import cleanup
import os
import image

# use this to test: python main.py sskaeeoh_tshirt.png 400 500 

def crossStitchParser(): 
    parser = argparse.ArgumentParser(description="Generate a cross stitch pattern from any image!")
    
    parser.add_argument('filepath', type=str, help='full file path to your image file')
    parser.add_argument('newfilename', type=str, help='the new filename to save your resized file, saved under build/')
    parser.add_argument('y', type=int, help='the number of desired pixels on the y axis')
    parser.add_argument('x', type=int, help = 'the number of desired pixels on the x axis')
    parser.add_argument('clean', type=bool, default = True, help='default True, deletes previously generated images under build/')
    return parser



if __name__ == "__main__": 

    parser = crossStitchParser()
    args = parser.parse_args()

    if args.clean: 
        cleanup.cleanup()

    if not os.path.exists(args.filepath):
        raise Exception(f"Filepath {args.filepath} is not found")

    print(f"Generating a {args.x} x {args.y} crossstitch pattern for {args.filepath} ")
    
    original_image = image.load_image(args.filepath)
    resized_image = image.resize_image(original_image, args.x, args.y)
    pixel_layer = image.get_pixel_layer(resized_image)
    os.makedirs("build", exist_ok=True)
    outputfile = "build/" + args.newfilename
    resized_image.save("build/blahblahblah.png")
