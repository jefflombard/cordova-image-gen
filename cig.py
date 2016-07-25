from sys import argv
from PIL import Image
from json import load
import os

# Functions
def check_input_image_size(image):

    # Define required image size
    required_width = 192
    required_height = 192

    # Get Image size data
    image_width = image.size[0]
    image_height = image.size[1]
    is_square = (image_width == image_height)
    is_large_enough = (image_width >= required_width and image_height >=
                       required_height)
    # Return Test

    if is_large_enough and is_square:
        return (True,"No Error")
    elif is_large_enough and (not is_square):
        return (False, "Image is not square. Please try again.")
    else:
        return (False, "Image is not large enough. Please try again with an image that is at least 192x192.")

def splash(color):
    pass

# Setup
# Input
# Transform
# Output

# Main

def icon(image):
    # Setup/Load
    with open('icons.json') as data:
        json = load(data)

    # Check if image size is big enough.
    print("Checking Image Size...")
    if check_input_image_size(image)[0]:
        print("Image size is good.")
    else:
        print(check_input_image_size(image)[1])
        return False

    # Make output directory
    print("Looking for output directory...")
    if not os.path.exists('output'):
        print("None found, making output directory. Output will be stored in /output")
        os.mkdir('output')
    else:
        print("Found! Output will be stored in /output")

    # Build Icons
    for platform in json:
        print('Generating '+platform+" icons...")
        if not os.path.exists("output/"+platform):
            os.mkdir('output/'+platform)
        for icon in json[platform]:
            image_size = json[platform][icon]
            icon_instance = image.resize((image_size,image_size),resample=3)
            print('output/'+platform+'/'+icon)
            icon_instance.save('output/'+platform+"/"+icon)


def main():
    # File Input -> Checks for valid image file
    try:
        image = Image.open(argv[1])
    except:
        # If I/O Error is through invalid image is passed as sys arg.
        print("Please select a valid image file")
        return False

    icon(image)

    if len(argv) > 2 and argv[2] == 'withSplash':
        pass

main()
