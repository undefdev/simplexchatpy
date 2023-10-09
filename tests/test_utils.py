import unittest
import json
from utils import encode_message, decode_message
from models import MessageContent, MessageContainer
from exceptions import EncodingError, DecodingError

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Sample message for testing
        self.message_obj = MessageContainer(
            content=MessageContent(type="text", content="test")
        )
        self.encoded_message = '{"content": {"type": "text", "content": "test"}, "file": null, "quote": null, "forward": false}'

    def test_encode_message(self):
        encoded = encode_message(self.message_obj)
        self.assertEqual(encoded, self.encoded_message)

    def test_decode_message(self):
        decoded = decode_message(self.encoded_message)
        self.assertIsInstance(decoded, MessageContainer)
        self.assertEqual(decoded.content.type, self.message_obj.content.type)
        self.assertEqual(decoded.content.content, self.message_obj.content.content)

    def test_encode_with_invalid_input(self):
        with self.assertRaises(EncodingError):
            encode_message(None)

    def test_decode_with_invalid_input(self):
        with self.assertRaises(DecodingError):
            decode_message("invalid json")

    def test_message_container_exclusivity(self):
        with self.assertRaises(ValueError):
            # Creating a MessageContainer with both `quote` and `forward` should raise a ValueError.
            MessageContainer(
                content=MessageContent(type="text", content="test"),
                quote="quoted_message_id",
                forward=True
            )

if __name__ == "__main__":
    unittest.main()

