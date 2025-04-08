from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: tag is none")
        if self.children is None:
            raise ValueError("Invalid HTML: children is none")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
            html_string += node.to_html()
        html_string += f"</{self.tag}>"
        return html_string