class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise Exception("NotImplementedError")

    def props_to_html(self, props=None):
        if not props:
            return ""
        result = ""
        for key, value in props.items():
            result += f" {key}='{value}'"
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if not value:
            raise ValueError("LeafNode requires a value")
        else:
            self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        
        props_to_html = f"{self.props_to_html(self.props)}" if self.props else ""
        
        return f"<{self.tag}{props_to_html}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if not tag:
            raise ValueError("ParentNode requires a value")
        else:
            self.tag = tag

        if not children:
            raise ValueError("ParentNode requires a children value")
        else:
            self.children

        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be empty")
        if not self.children:
            raise ValueError("children value cannot be empty")
        
 


        
    

