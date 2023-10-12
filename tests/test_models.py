import unittest
from models import MessageContent, TextContent, LinkContent, ImageContent, FileContent
from dataURI import DataURI

class TestMessageContent(unittest.TestCase):

    def test_text_content_non_empty(self):
        content = TextContent(text="Hello, World!")
        self.assertEqual(content.type, "text")
        self.assertEqual(content.content, {"text": "Hello, World!"})

    def test_text_content_empty(self):
        with self.assertRaises(ValueError):
            TextContent(text="")

    def test_link_content_non_empty(self):
        content = LinkContent(text="www.example.com", preview="Check this out!")
        self.assertEqual(content.type, "link")
        self.assertEqual(content.content, {"text": "www.example.com", "preview": "Check this out!"})

    def test_link_content_empty(self):
        with self.assertRaises(ValueError):
            LinkContent(text="", preview="This link is empty!")

    def test_image_content(self):
        # Assuming DataURI class has a __str__ method that returns a string representation.
        dummy_image_data = "data:image/webp;base64,UklGRkAAAABXRUJQVlA4IDQAAADwAQCdASoBAAEAAQAcJaACdLoB+AAETAAA/vW4f/6aR40jxpHxcP/ugT90CfugT/3NoAAA"
        dummy_image = DataURI(dummy_image_data)
        content = ImageContent(text="Look at this image!", image=dummy_image_data)
        self.assertEqual(content.type, "image")
        self.assertEqual(content.content, {"text": "Look at this image!", "image": dummy_image})

    def test_file_content(self):
        content = FileContent(text="Here's a file!")
        self.assertEqual(content.type, "file")
        self.assertEqual(content.content, {"text": "Here's a file!"})

    def test_unrecognized_type_with_text(self):
        content = MessageContent(type="unknown", content={"text": "This is some unknown content."})
        self.assertEqual(content.type, "text")
        self.assertEqual(content.content, {"from": "unknown", "text": "This is some unknown content."})

    def test_unrecognized_type_without_text(self):
        with self.assertRaises(ValueError):
            MessageContent(type="unknown", content={})

if __name__ == "__main__":
    unittest.main()

