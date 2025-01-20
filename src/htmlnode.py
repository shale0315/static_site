class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self. value = value
        self. children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = list(self.props)
        converted = ""
        for item in props_list:
            converted += f' {item}="{self.props[item]}"'
        return converted
    
    def __eq__(self,other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if not self.tag:
            return self.value
        if self.tag != "img":
            if not self.value:
                raise ValueError("No value")
            if self.props:
                converted = self.props_to_html()
                return f'<{self.tag}{converted}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
        elif self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}>'
 
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        html_string = ""
        if not self.tag:
            raise ValueError("No tag")
        if not self.children:
            raise ValueError("No children")
        for child in self.children:
            html_string += child.to_html()
        final_string = f"<{self.tag}>{html_string}</{self.tag}>"
        return final_string

