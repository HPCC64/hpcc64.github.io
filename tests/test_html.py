import unittest
from html.parser import HTMLParser

class TestIndexHTML(unittest.TestCase):
    def test_parse_index_html(self):
        parser = HTMLParser()
        with open('index.html', encoding='utf-8') as f:
            content = f.read()
        try:
            parser.feed(content)
        except Exception as e:
            self.fail(f"HTML parsing failed: {e}")

if __name__ == '__main__':
    unittest.main()
