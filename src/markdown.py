from textnode import TextType, TextNode


# takes a list of nodes and splits any TEXT nodes containing the delimeter into multiple nodes
#   updates and returns the new list of nodes
def split_nodes_delimiter(old_nodes, delimeter, text_type):
    if len(old_nodes) == 0: return old_nodes

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimeter)
        num_segs = len(split_text)
        
        if num_segs == 1:
            # delimeter not found
            new_nodes.append(node)
        
        elif num_segs > 1 and num_segs % 2 == 0:
            # invalid markdown (even number of segments)
            raise Exception("Closing delimeter not found")
        
        elif num_segs > 1 and num_segs % 2 == 1:
            # valid split (odd number of segments)
            for i, seg in enumerate(split_text):
                new = None
                # every odd element is within the delimters; even is plain text
                if i % 2 == 1:
                    new = TextNode(seg, text_type)
                else:
                    new = TextNode(seg, TextType.TEXT)
                new_nodes.append(new)

    return new_nodes

                
# TODO : add test_markdown.py file




