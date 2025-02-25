

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        if tag == None: assert value != None and props == None
        if value == None: assert children != None
        if children == None: assert value != None

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # determine if two HTMLNodes are equal
    def __eq__(self, other):
        if not isinstance(other, HTMLNode): return False
        return self.tag == other.tag and\
               self.value == other.value and\
               self.children == other.children and\
               self.props == other.props

    # overriden by children to render themselves as HTML
    def to_html(self):
        raise NotImplementedError
    
    # returns dict of attributes as a whitespace separated string, None otherwise
    def props_to_html(self):
        if not self.props: return None
        output = ""
        for attribute in self.props:
            output += f"{attribute}=\"{self.props[attribute]}\" "
        return output.rstrip()
    
    # returns printable representation of HTML node
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    # convert node to html
    def to_html(self):
        if self.value == None: 
            raise ValueError("Missing value")
        if self.tag == None: 
            return self.value
        
        output = ""
        # open tag; add attributes if any
        attributes = self.props_to_html()
        if attributes: 
            output += f"<{self.tag} {attributes}>"
        else:
            output += f"<{self.tag}>"

        # add text
        output += self.value

        # close tag
        output += f"</{self.tag}>"
        
        return output


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        if self.children == None:
            raise ValueError("Node has no children")

        output = ""
        # open tag; add attributes if any
        attributes = self.props_to_html()
        if attributes: 
            output += f"<{self.tag} {attributes}>"
        else:
            output += f"<{self.tag}>"

        # convert all children to html and concatenate to output
        for child in self.children:
            if child == None:
                raise ValueError("Missing child")
            output += child.to_html()

        # close tag
        output += f"</{self.tag}>"
        
        return output
        


