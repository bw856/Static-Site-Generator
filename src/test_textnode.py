import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_b1 = TextNode("bold text node", TextType.BOLD)
        node_b2 = TextNode("bold text node", TextType.BOLD)
        self.assertEqual(node_b1, node_b2)

    #@unittest.skip("test neq later")
    def test_neq(self):
        node_normal = TextNode("normal text node", TextType.NORMAL)
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
        no_url = TextNode("normal text node", TextType.NORMAL)
        with_url = TextNode("normal text node", TextType.NORMAL, "https://boot.dev")
        assert no_url.url == None
        assert with_url.url == "https://boot.dev"
        self.assertNotEqual(no_url, with_url)

        


if __name__ == "__main__":
    unittest.main()