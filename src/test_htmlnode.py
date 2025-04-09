import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
