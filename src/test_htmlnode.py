
import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    # test default values
    def test_none(self):
        child = HTMLNode(value="some text")
        no_tag = HTMLNode(              value="text", children=[child], props=None)
        no_value = HTMLNode(   tag="p",               children=[child], props="")
        no_children = HTMLNode(tag="p", value="text",                   props="")
        no_props = HTMLNode(   tag="p", value="text", children=[child])

        assert None == no_tag.tag == no_value.value == no_children.children == no_props.props

    # test props_to_html()
    def test_props(self):
        node0 = HTMLNode(tag="p", value="some text")
        self.assertEqual(node0.props_to_html(), None)

        node1 = HTMLNode(tag="p", value="some text", props={"href": "https://www.google.com"})
        self.assertEqual(node1.props_to_html(),
                          "href=\"https://www.google.com\"")

        node2 = HTMLNode("p", "some text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.props_to_html(),
                          "href=\"https://www.google.com\" target=\"_blank\"")
    
    # test repr
    def test_print(self):
        node = HTMLNode("p", "this is some text", None, {"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(repr(node), 
                         "HTMLNode(p, this is some text, None, {'href': 'https://www.google.com', 'target': '_blank'})")
                         
        child = HTMLNode(value="some text")
        with_child = HTMLNode("p", "this is some text", child, {"href": "https://www.google.com", "target": "_blank"})
 
        self.assertEqual(repr(with_child), 
                         "HTMLNode(p, this is some text, HTMLNode(None, some text, None, None), {'href': 'https://www.google.com', 'target': '_blank'})")
        
    # test LeafNode subclass
    def test_leaf_to_html(self):
        leaf = LeafNode("p", "some text", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(leaf.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">some text</p>")

        no_tag = LeafNode(tag=None, value="some text")
        self.assertEqual(no_tag.to_html(), "some text")

        with self.assertRaises(TypeError):
            no_value = LeafNode(tag="p", props={"href": "https://www.google.com"})
        
        no_value = LeafNode(tag="p", value="remove this", props={"href": "https://www.google.com"})
        no_value.value = None
        with self.assertRaises(ValueError):
            no_value.to_html()

    # test ParentNode subclass
    def test_parent_to_html(self):
        basic = ParentNode("p", 
                            [LeafNode("b", "bold text"), 
                             LeafNode(None, "normal text"), 
                             LeafNode("i", "italic text"),
                             LeafNode(None, "normal text")],)
        self.assertEqual(basic.to_html(), 
                         "<p><b>bold text</b>normal text<i>italic text</i>normal text</p>")
        
        attributes = ParentNode("p", 
                            [LeafNode("b", "bold text", {"target": "_blank"}), 
                             LeafNode(None, "normal text"),],
                             props={"href": "https://www.google.com"})
        self.assertEqual(attributes.to_html(), 
                         "<p href=\"https://www.google.com\"><b target=\"_blank\">bold text</b>normal text</p>")
         
        empty_child = ParentNode("p", [])
        self.assertEqual(empty_child.to_html(), "<p></p>")

        multiple_parents = ParentNode("p", 
                                      [ParentNode("li", 
                                                  [LeafNode("b", "bold text", {"target" : "_blank"})],
                                                  {"href" : "https://boot.dev"}
                                                  )])
        self.assertEqual(multiple_parents.to_html(), 
                         "<p><li href=\"https://boot.dev\"><b target=\"_blank\">bold text</b></li></p>")
            

        with self.assertRaises(TypeError):
            no_tag = ParentNode(children=[LeafNode("p", "some text")], props={"href": "https://www.google.com"})
            no_children = ParentNode(tag="p", props={"href": "https://www.google.com"})
        
        no_tag = ParentNode(tag="remove this", children=[LeafNode("p", "some text")], props={"href": "https://www.google.com"})
        no_tag.tag = None
        with self.assertRaises(ValueError):
            no_tag.to_html()

        no_child = ParentNode(tag="remove this", children=[LeafNode("p", "some text")], props={"href": "https://www.google.com"})
        no_child.children = None
        with self.assertRaises(ValueError):
            no_tag.to_html()

        




if __name__ == "__main__":
    unittest.main()