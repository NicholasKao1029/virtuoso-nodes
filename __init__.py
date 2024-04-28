from .blendmodes import BlendModes
from .selectivecolor import SelectiveColor
from .colors import SolidColor
from .colors import SplitRGB
from .colors import MergeRGB

NODE_CLASS_MAPPINGS = {
    "BlendModes": BlendModes,
    "SelectiveColor": SelectiveColor,
    "SolidColor": SolidColor,
    "SplitRGB": SplitRGB,
    "MergeRGB": MergeRGB
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BlendModes": "Blend Modes",
    "SelectiveColor": "Selective Color",
    "SolidColor": "Solid Color Image",
    "SplitRGB": "Split RGB",
    "MergeRGB": "Merge RGB"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']