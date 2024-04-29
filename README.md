# Virtuoso Nodes for ComfyUI

This set of nodes is designed to give some Photoshop-like functionality within ComfyUI. The nodes available are:

1. **Blend Modes**: Applies an image to another image using a blend mode operation. Every conceivable blend mode is available!
2. **Solid Color Image**: This node allows you to create an image of a single color. These can be very useful in conjunction with the blend modes.
3. **SplitRGB**: This node takes an image and splits it into its red, green, and blue components. These then can be used in creative ways with blend modes as well.
4. **MergeRGB**: This node takes three images, and merges the specified channels into one image. It is the complementary node to the SplitRGB node, to be used to recombine channels that you have split, though you can feel free to merge any images you wish for trippy effects.
<br>

## Blend Modes

![Blend Modes Node Image](https://github.com/chrisfreilich/virtuoso-nodes/assets/108036952/baf71856-aefa-4ffb-9972-fc0b7e165956)

This node gives access to thirty different blend modes, and includes a scaling option for the top layer and the ability to use external masks.

### Node controls:

- **backdrop**: This is the background image. The output image will have the same dimensions as this image.
- **source**: This is the top image. If it is not the same size as the backdrop image, it will be resized to cover the backdrop.
- **mask**: Can be used to retain the alpha channel from the source image, or you can use an external mask to control the blended area.
- **opacity**: The opacity of the source image. The backdrop image is always 100% opacity. 
- **source_adjust**: The method by which the source image will be resized if necessary.
     - *Stretch* will change each dimension independently just as much as needed to match that dimension, potentially changing the aspect ratio of the source image and causing distortion.
     - *Crop* will maintain the aspect ratio of the source image, and resize it until it just covers the backdrop image, then crop what doesn't fit.
- **blend_mode**: normal is the default blend mode.

### Examples
[Normal](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/normal-modes.md)
[Darken](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/darken-modes.md)
[Lighten](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/lighten-modes.md)
[Contrast](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/contrast-modes.md)
[Component](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/component-modes.md)
[Specialty](https://github.com/chrisfreilich/virtuoso-nodes/blob/main/specialty-mode.md)

Learn about the math behind blend modes here: https://learning.hccs.edu/faculty/bradly.brown/arts2348/handouts/blending-modes  
A practical discussion of the blend modes is here: https://www.youtube.com/watch?v=i1D9ijh3_-I
<br><br>

## Blend If Node

![image](https://github.com/chrisfreilich/virtuoso-nodes/assets/108036952/cab68d47-454b-4ae3-860b-f7d999caec2c)

This node gives you the functionality that is available with Photoshop's Blend If feature:

![Screenshot 2024-04-29 164742](https://github.com/chrisfreilich/virtuoso-nodes/assets/108036952/5743979f-62d5-4a37-96c1-12b91d6eb3a4)

This feature composites the top_layer image over the bottom_layer image based on various possible calculations. ComfyUI's interface options being limited, the inputs have all been converted to fields instead of nice sliders.

### Node input controls:

- **top_layer**: This is the top image. If it is not the same size as the bottom_layer image, it will be resized to cover the bottom layer. This is equivalent to 'current layer' in Photoshop.
- **bottom_layer**: This is the background image. The output image will have the same dimensions as this image. This is equivalent to 'underlying layer' in Photoshop.
- **mask**: This is an optional mask for the top layer, which will add to the transparency of the top layer in addition to the transparency created by the Blend If process. Any alpha channels in the top_layer and bottom_layer images are ignored.
- **blend_if_layer**: Choose the layer that will be analyzed to determine the opacity of the top layer. This is equivalent to Photoshop's 'current layer' and 'underlying layer' sliders. This node only calculates one or the other.
- **blend_if_channel**: Which color channel (or gray) will be used to analyze the selected layer. This is equivalent to the "Blend If:" dropdown in photoshop.
- **start_rise, end_rise, start_fall, end_fall**: These four inputs define which brightness values for the selected channel on the selected layer are opaque. They are equivalent to the triangles below the 'current layer' and 'underlying layer' sliders, which each split into two to add softness to the selection. In this node, any brightness values lower than start_rise or greater than end_fall will be completely transparent, and brightness values between end_rise and start_fall will be completely opaque. Brightness values between start_rise and end_rise and between start_fall and end_fall will be partially transparent to feather the edges of the selection.
- **opacity**: Values less than 1 will reduce the opacity of the top_layer image in addition to any transparency calculated by the Blend If process. This is the equivalent to the opacity setting for the entire layer in Photoshop.
- **match_size**: Method to use to resize the top_layer image if it is not the same size as the bottom_layer image.
- **invert_mask**: 'yes' will invert the incoming mask before applying it to the top_layer image. Set to 'yes' by default, as it seems to be the more common situation.

### Node Outputs
- **IMAGE**: The final image with top_layer composited on top of bottom_layer.
- **MASK**: This is the mask generated by the Blend If process. It can be useful to ensure you are getting the result you want, or to do further processing on the same pixels.
<br>

## Solid Color Image

![image](https://github.com/chrisfreilich/virtuoso-nodes/assets/108036952/d2fea774-a390-4adc-a2d5-4f475c508acf)

This node creates an image of a single color. This can be particularly useful for many of the blend modes. When using as the source image of a blend mode mode, the size is unimportant as it will be stretched to fit.

### Node controls:

- **RGB**: You can enter the red, green, and blue levels manually, or use the circle on the right to bring up a color picker. The color picker window appears at the top left of the screen.
- **size**: Enter the width and height of the image. If you're using the image as the source for a blending mode, you can set both values to 1 to save space, as it will be stretched to fit.
<br>

## Split RGB and Merge RGB 

![image](https://github.com/chrisfreilich/virtuoso-nodes/assets/108036952/d8ae9988-5f5b-43da-bfaa-15b9778f1959)

These nodes split apart images into their component color channels and merge them back together. You can do fun things with the layers once they're separate, and then combine them back together when you're done. If you want even more control when merging them back together, you can use the Linear Dodge (Add) blend mode instead (twice), which will accomplish the same thing while giving you the ability to play around with the opacities of each layer.

### Node controls:

- **image**: The image to split on the Split RGB node, and the merged image on the Merge RGB node
- **red, green, blue**: The separate images holding the red, green, and blue channels of the image. Note that there is nothing stopping you from using any images you want here on the Merge RGB node-- the node will only take the indicated color channel from each image.
  
# Installation:

1. Git clone this repo into a folder in ComfyUI\custom_nodes
2. pip install -r requirements.txt

**Please let me know if you have any thoughts or suggestions!**
<br><br>




