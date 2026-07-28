

class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html = ""
        if self.props is None or len(self.props) == 0:
            html = ""
        else:
            for prop in self.props:
                html += f' {prop}="{self.props[prop]}"'
        return html

    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        html = ''
        if self.value is None or self.value == "":
            raise ValueError("No value")
        if self.tag is None or self.tag == "":
            html = self.value
        else:
            prop = super().props_to_html()
            html = f"<{self.tag}{prop}>{self.value}</{self.tag}>"
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

