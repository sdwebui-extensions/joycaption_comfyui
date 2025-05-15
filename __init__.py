from . import nodes

NODE_CLASS_MAPPINGS = {
	"JJC_JoyCaption": nodes.JoyCaption,
	"JJC_JoyCaption_Custom": nodes.JoyCaptionCustom,
    "JJC_JoyCaptionModelLoad": nodes.JoyCaptionModelLoad,
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"JJC_JoyCaption": "JJC JoyCaption",
	"JJC_JoyCaption_Custom": "JJC JoyCaption (Custom)",
    "JJC_JoyCaptionModelLoad": "JJC JoyCaption Model Load"
}
