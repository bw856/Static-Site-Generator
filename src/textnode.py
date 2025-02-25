from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode): return False
        return self.text == other.text\
            and self.text_type == other.text_type\
            and self.url == other.url 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

# convert TextNode to HTMLNode (LeafNode)
def text_node_to_html_node(text_node):
    type = text_node.text_type
    tag = None
    text = None
    props = None

    if type == TextType.TEXT:
        text = text_node.text
    elif type == TextType.BOLD:
        tag = "b"
        text = text_node.text
    elif type == TextType.ITALIC:
        tag = "i"
        text = text_node.text
    elif type == TextType.CODE:
        tag = "code"
        text = text_node.text
    elif type == TextType.LINK:
        tag = "a"
        text = text_node.text
        props = {"href": text_node.url}
    elif type == TextType.IMAGE:
        tag = "img"
        text = ""
        props = {"src": text_node.url, "alt": text_node.text}
    else:
        raise Exception("Invalid Text Type")

    return LeafNode(tag, text, props)