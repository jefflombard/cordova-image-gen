from sys import argv
from PIL import Image, ImageColor
from json import load
from re import match
import os

# Functions for use in main()
def check_input_image_size(image):

    # Define required image size
    required_width = 192
    required_height = 192

    # Get Image size data
    image_width = image.size[0]
    image_height = image.size[1]
    is_square = (image_width == image_height)
    is_large_enough = (image_width >= required_width and image_height >= required_height)
    # Return Test

    if is_large_enough and is_square:
        return (True,"No Error")
    elif is_large_enough and (not is_square):
        return (False, "Image is not square. Please try again.")
    else:
        return (False, "Image is not large enough. Please try again with an image that is at least 192x192.")

def check_color(color):
    # Use regex to validate hexcode
    re_result = match('#(\w{6})', color)
    # Need an if statement, otherwise returning re_result will result in a RE Object
    if re_result:
        return True
    else:
        return False

def splash(color):
    output_path = 'output/screen/'
    with open('splash.json') as data:
        json = load(data)

    # Make output directory
    if not os.path.exists(output_path):
        os.mkdir('output/screen/')

    # Build Splash
    for platform in json:
        print('Generating '+platform+" splash screens...")
        if not os.path.exists(output_path+platform):
            os.mkdir(output_path+platform)
        for splash in json[platform]:
            image_width = json[platform][splash][0]
            image_height = json[platform][splash][1]
            # Generate image file
            make = Image.new('RGB',(image_width,image_height),color)
            make.save(output_path+platform+'/'+splash)


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

    icon_xml = """
    <!-- Copy this code into config.xml -->
    <platform name="ios">
        <!-- iOS 8.0+ -->
        <!-- iPhone 6 Plus  -->
        <icon src="res/ios/icon-60@3x.png" width="180" height="180" />
        <!-- iOS 7.0+ -->
        <!-- iPhone / iPod Touch  -->
        <icon src="res/ios/icon-60.png" width="60" height="60" />
        <icon src="res/ios/icon-60@2x.png" width="120" height="120" />
        <!-- iPad -->
        <icon src="res/ios/icon-76.png" width="76" height="76" />
        <icon src="res/ios/icon-76@2x.png" width="152" height="152" />
        <!-- iOS 6.1 -->
        <!-- Spotlight Icon -->
        <icon src="res/ios/icon-40.png" width="40" height="40" />
        <icon src="res/ios/icon-40@2x.png" width="80" height="80" />
        <!-- iPhone / iPod Touch -->
        <icon src="res/ios/icon.png" width="57" height="57" />
        <icon src="res/ios/icon@2x.png" width="114" height="114" />
        <!-- iPad -->
        <icon src="res/ios/icon-72.png" width="72" height="72" />
        <icon src="res/ios/icon-72@2x.png" width="144" height="144" />
        <!-- iPhone Spotlight and Settings Icon -->
        <icon src="res/ios/icon-small.png" width="29" height="29" />
        <icon src="res/ios/icon-small@2x.png" width="58" height="58" />
        <!-- iPad Spotlight and Settings Icon -->
        <icon src="res/ios/icon-50.png" width="50" height="50" />
        <icon src="res/ios/icon-50@2x.png" width="100" height="100" />
    </platform>
    <platform name="android">
        <!--
            ldpi    : 36x36 px
            mdpi    : 48x48 px
            hdpi    : 72x72 px
            xhdpi   : 96x96 px
            xxhdpi  : 144x144 px
            xxxhdpi : 192x192 px
        -->
        <icon src="res/android/ldpi.png" density="ldpi" />
        <icon src="res/android/mdpi.png" density="mdpi" />
        <icon src="res/android/hdpi.png" density="hdpi" />
        <icon src="res/android/xhdpi.png" density="xhdpi" />
        <icon src="res/android/xxhdpi.png" density="xxhdpi" />
        <icon src="res/android/xxxhdpi.png" density="xxxhdpi" />
    </platform>
    """

    print("Don't forget to copy the html in _text_output.txt into config.xml")

    # Make Text file

    with open('output/_text_output.txt', 'w+') as data:
        data.write(icon_xml)

    # Checks for Splash Screen
    if len(argv) > 2 and argv[2] == '-ws':
        color = input("Enter the hex color for the splash screen (including the # sign):")
        while check_color(color) == False:
            if color == 'q':
                return False
            color = input("Please enter a valid hex value preceded by a # or 'q' to quit:")

        splash(color)
        splash_xml = """

    <platform name="android">
        <!-- you can use any density that exists in the Android project -->
        <splash src="res/screen/android/splash-land-hdpi.png" density="land-hdpi"/>
        <splash src="res/screen/android/splash-land-ldpi.png" density="land-ldpi"/>
        <splash src="res/screen/android/splash-land-mdpi.png" density="land-mdpi"/>
        <splash src="res/screen/android/splash-land-xhdpi.png" density="land-xhdpi"/>

        <splash src="res/screen/android/splash-port-hdpi.png" density="port-hdpi"/>
        <splash src="res/screen/android/splash-port-ldpi.png" density="port-ldpi"/>
        <splash src="res/screen/android/splash-port-mdpi.png" density="port-mdpi"/>
        <splash src="res/screen/android/splash-port-xhdpi.png" density="port-xhdpi"/>
    </platform>

    <platform name="ios">
        <!-- images are determined by width and height. The following are supported -->
        <splash src="res/screen/ios/Default~iphone.png" width="320" height="480"/>
        <splash src="res/screen/ios/Default@2x~iphone.png" width="640" height="960"/>
        <splash src="res/screen/ios/Default-Portrait~ipad.png" width="768" height="1024"/>
        <splash src="res/screen/ios/Default-Portrait@2x~ipad.png" width="1536" height="2048"/>
        <splash src="res/screen/ios/Default-Landscape~ipad.png" width="1024" height="768"/>
        <splash src="res/screen/ios/Default-Landscape@2x~ipad.png" width="2048" height="1536"/>
        <splash src="res/screen/ios/Default-568h@2x~iphone.png" width="640" height="1136"/>
        <splash src="res/screen/ios/Default-667h.png" width="750" height="1334"/>
        <splash src="res/screen/ios/Default-736h.png" width="1242" height="2208"/>
        <splash src="res/screen/ios/Default-Landscape-736h.png" width="2208" height="1242"/>
    </platform>"""
        with open('output/_text_output.txt', 'a') as data:
            data.write(splash_xml)

main()
