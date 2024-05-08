import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_repr(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, Hello, world!, children: None, {'class': 'greeting', 'href': 'https://boot.dev'})",
        )


if __name__ == "__main__":
    unittest.main()
