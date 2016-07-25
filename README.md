# cordova-image-gen

Simple python script to generate icons, splash screens, and the proper text for config.xml.

## Installation

1. Clone this repo to a desired location on your system running:
	`git clone https://github.com/jefflombard/cordova-image-gen.git`

### Requirements

Cordova-image-gen uses `Python 3.5` and `Pillow 3.3.0`.

To install Pillow run `pip install Pillow` in bash.

## Generating Icons

1. Using bash/terminal window navigate to the cloned repo.
2. Add a source image that can be used to generate icons in the `/cordova-image-gen` directory. (Must be at least 192 x 192 px)
3. Run the following command in bash `python cig.py <filename>`
4. This will then create a folder with the generated icons `/output` in the `/cordova-image-gen` directory
5. Copy the contents of `/output` to `/res` in your cordova project.
6. Be sure to add the contents from `_text_output.txt` to `config.xml`

_Note: Currently this only generates images for iOS and Android_

### Generating Splash Screens

You can also generate splash screens using the `-ws` flag when runnning `cig.py`.

*Example:* `python cig.py icon_source.png -ws`

You will be prompted for a hex color code for the splash screen. Enter your color code and splash screens will be created in `/output	/screen`