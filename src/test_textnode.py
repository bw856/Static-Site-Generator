import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_b1 = TextNode("bold text node", TextType.BOLD)
        node_b2 = TextNode("bold text node", TextType.BOLD)
        self.assertEqual(node_b1, node_b2)

    def test_neq(self):
        node_normal = TextNode("normal text node", TextType.TEXT)
        node_bold = TextNode("bold text node", TextType.BOLD)
        node_italic = TextNode("italic text node", TextType.ITALIC)
        node_code = TextNode("code text node", TextType.CODE)
        node_link = TextNode("link text node", TextType.LINK)
        node_image = TextNode("image text node", TextType.IMAGE)
        self.assertNotEqual(node_normal, node_bold)
        self.assertNotEqual(node_normal, node_italic)
        self.assertNotEqual(node_normal, node_code)
        self.assertNotEqual(node_normal, node_link)
        self.assertNotEqual(node_normal, node_image)
    
    def test_url(self):
        no_url = TextNode("normal text node", TextType.TEXT)
        with_url = TextNode("normal text node", TextType.TEXT, "https://google.com")
        assert no_url.url == None
        assert with_url.url == "https://google.com"
        self.assertNotEqual(no_url, with_url)

    # test the text_node_to_html_node function
    def test_textnode_to_htmlnode(self):
        node_normal = TextNode("normal", TextType.TEXT)
        node_bold = TextNode("bold", TextType.BOLD)
        node_italic = TextNode("italic", TextType.ITALIC)
        node_code = TextNode("code text", TextType.CODE)
        node_link = TextNode("link", TextType.LINK, "https://google.com")
        node_image = TextNode("image text", TextType.IMAGE, "https://google.com")
        node_none = TextNode("typeless", None)

        self.assertEqual(text_node_to_html_node(node_normal), LeafNode(None, "normal"))
        self.assertEqual(text_node_to_html_node(node_bold), LeafNode("b", "bold"))
        self.assertEqual(text_node_to_html_node(node_italic), LeafNode("i", "italic"))
        self.assertEqual(text_node_to_html_node(node_code), LeafNode("code", "code text"))
        self.assertEqual(text_node_to_html_node(node_link), LeafNode("a", "link", {"href":"https://google.com"}))
        self.assertEqual(text_node_to_html_node(node_image), LeafNode("img", "", {"src":"https://google.com", "alt":"image text"}))
        with self.assertRaises(Exception):
            text_node_to_html_node(node_none)



if __name__ == "__main__":
    unittest.main()