# Upscaler
a CLI tool to upscale images written in Python.


## How to use
The local-upscale.py script is a command-line utility for upscaling images. It takes four arguments:

+ `image_path`: The path to the image file you want to upscale.
+ `upscale_percentage`: The percentage by which you want to upscale the image.
+ `resampling_option`: The resampling method you want to use. This should be an integer between 1 and 4, where:
  + 1 is `Nearest Neighbor`
  + 2 is `Bilinear`
  + 3 is `Bicubic`
  + 4 is `Lanczos`
+ `output_path`: The path where you want to save the upscaled image.

You can run the script from the command line like this:

  `python local-upscale.py <image_path> <upscale_percentage> <resampling_option> <output_path>`

Replace <image_path>, <upscale_percentage>, <resampling_option>, and <output_path> with your actual values.

For example:

`python local-upscale.py "input-images/myimage.jpg" 200 3 "output-images/myimage_upscaled.jpg"`

This will upscale myimage.jpg by 200% using the Bicubic resampling method and save the result as myimage_upscaled.jpg in the output-images directory.

## help flag
You can get more information about each argument by running the script with the `-h` or `--help` option:
`python local-upscale.py --help`
This will display a help message with a description of the script and its arguments.
