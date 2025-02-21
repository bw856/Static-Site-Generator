from textnode import *
from htmlnode import *

""" TODO
def text_node_to_html_node(text_node):
    type = text_node.text_type

    if type == TextType.NORMAL:
        
    elif type == TextType.BOLD:

    elif type == TextType.ITALIC:

    elif type == TextType.CODE:

    elif type == TextType.LINK:

    elif type == TextType.IMAGE:
    
    else:
        raise Exception("Invalid Text Type")
"""



def main():
    text_node = TextNode("this is some text", TextType.NORMAL, "https://www.boot.dev")

    print(text_node)


main()