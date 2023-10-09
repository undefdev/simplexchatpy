import unittest
from dataURI import DataURI

class TestDataURI(unittest.TestCase):

    def test_valid_data_uri(self):
        # This should work without raising an exception
        # TODO: Consider testing more image types https://www.iana.org/assignments/media-types/media-types.xhtml#image
        valid = [
            "data:image/webp;base64,UklGRkAAAABXRUJQVlA4IDQAAADwAQCdASoBAAEAAQAcJaACdLoB+AAETAAA/vW4f/6aR40jxpHxcP/ugT90CfugT/3NoAAA",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAZABkAAD/2wCEABQQEBkSGScXFycyJh8mMi4mJiYmLj41NTU1NT5EQUFBQUFBREREREREREREREREREREREREREREREREREREREQBFRkZIBwgJhgYJjYmICY2RDYrKzZERERCNUJERERERERERERERERERERERERERERERERERERERERERERERERERP/AABEIAAEAAQMBIgACEQEDEQH/xABMAAEBAAAAAAAAAAAAAAAAAAAABQEBAQAAAAAAAAAAAAAAAAAABQYQAQAAAAAAAAAAAAAAAAAAAAARAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AJQA9Yv/2Q=="
        ]
        for uri in valid:
            data_uri_instance = DataURI(uri)
            self.assertEqual(data_uri_instance.value, uri)

    def test_invalid_data_uri(self):
        # This should raise a ValueError due to invalid format
        invalid_data_uri = "data:text/plain;base64,SGVsbG8sIFdvcmxkIQ=="
        with self.assertRaises(ValueError) as context:
            DataURI(invalid_data_uri)
        self.assertIn("not a valid data URI format", str(context.exception))

if __name__ == "__main__":
    unittest.main()
