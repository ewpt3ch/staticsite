import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            "p", 
            "a nice paragraph we have here", 
            None, 
            {"style": "bold"}
        )
        self.assertEqual(f' style="bold"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "p", 
            "a nice paragraph we have here", 
            None, 
            {"style": "bold"}
        )
        self.assertEqual("HTMLNode(p, a nice paragraph we have here, children: None, {'style': 'bold'})", node.__repr__())

    def test_values(self):
        node = HTMLNode(
                "div",
                "this is boring"
        )
        self.assertEqual(
                node.tag,
                "div"
        )

        self.assertEqual(
                node.value,
                "this is boring"
        )
        self.assertEqual(
                node.children, 
                None
        )
        self.assertEqual(
                node.props,
                None
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        child1 = LeafNode("b", "child1")
        child2 = LeafNode("i", "child2")
        parent = ParentNode("a", [child1, child2], {"href": "www.google.com"})
        self.assertEqual(parent.to_html(),
                         '<a href="www.google.com"><b>child1</b><i>child2</i></a>'
        )


if __name__ == "__main__":
    unittest.main()
