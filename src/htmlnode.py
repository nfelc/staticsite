class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ''
        props = self.props.items()
        for prop in props:
            html += f" {prop[0]}=\"{prop[1]}\"" 
        return html

    def __repf__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return  f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repf__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("invalid HTML: no tag")
        elif self.children is None:
            raise ValueError ("invalid HTML: parent node requires children")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return  f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
            
