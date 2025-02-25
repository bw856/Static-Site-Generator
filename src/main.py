from textnode import *
from htmlnode import *


def main():
    text_node = TextNode("this is some text", TextType.NORMAL, "https://www.boot.dev")

    print(text_node)


main()