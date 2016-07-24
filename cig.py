from sys import argv
from PIL import Image

# Functions
def check_input_image_size(image):

    # Define required image size
    required_width = 1024
    required_height = 1024
    
    # Get Image size data
    image_width = image.size[0]
    image_height = image.size[1]
    is_square = (image_width == image_height)
    is_large_enough = (image_width >= required_width and image_height >=
                       required_height)
    # Return Test
    if is_large_enough and is_square:
        return (True)
    elif is_large_enough and not is_square:    
        return (False, "Image is not square. Please try again.")
    else:
        return (False, "Image is not large enough. Please try again.")

# Setup
# Input
# Transform
# Output

# Main

def main():

    # File Input -> Checks for valid image file
    try:
        image = Image.open(argv[1])
    except:
        # If I/O Error is through invalid image is passed as sys arg.
        print("Please select a valid image file")
        return False
    # Check if image size is big enough.
    print("Checking Image Size...")
    if check_input_image_size(image)[0]:
        print("Image size is good.")
    else:
        print(check_input_image_size(image)[1])
        return False



main()
