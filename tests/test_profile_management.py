import unittest
from chat import SimplexChat
from exceptions import EncodingError

class TestSimplexChatProfileManagement(unittest.TestCase):

    def setUp(self):
        self.chat = SimplexChat()

    def test_update_without_setting_profile(self):
        # Attempting to update a profile that hasn't been set should raise an error.
        with self.assertRaises(Exception):
            self.chat.update_profile(display_name="JaneDoe")

    def test_delete_without_setting_profile(self):
        # Attempting to delete a profile that hasn't been set should raise an error.
        with self.assertRaises(Exception):
            self.chat.delete_profile()

    def test_set_profile(self):
        self.chat.set_profile(display_name="JohnDoe", full_name="John Doe")
        profile = self.chat.get_profile()
        self.assertEqual(profile.displayName, "JohnDoe")
        self.assertEqual(profile.fullName, "John Doe")

    def test_update_profile(self):
        self.chat.set_profile(display_name="JohnDoe", full_name="John Doe")
        self.chat.update_profile(display_name="JaneDoe")
        profile = self.chat.get_profile()
        self.assertEqual(profile.displayName, "JaneDoe")
        self.assertEqual(profile.fullName, "John Doe")

    def test_delete_profile(self):
        self.chat.set_profile(display_name="JohnDoe", full_name="John Doe")
        self.chat.delete_profile()
        profile = self.chat.get_profile()
        self.assertIsNone(profile)

    def test_validate_display_name(self):
        with self.assertRaises(ValueError):
            self.chat.validate_display_name("") # empty display names are forbidden
        with self.assertRaises(ValueError):
            self.chat.validate_display_name("#InvalidName")
        with self.assertRaises(ValueError):
            self.chat.validate_display_name("@InvalidName")
        with self.assertRaises(ValueError):
            self.chat.validate_display_name(" InvalidName")
        with self.assertRaises(ValueError):
            self.chat.validate_display_name("Invalid Name")

    def test_profile_image_set_and_change(self):
        image1 = "data:image/webp;base64,UklGRkAAAABXRUJQVlA4IDQAAADwAQCdASoBAAEAAQAcJaACdLoB+AAETAAA/vW4f/6aR40jxpHxcP/ugT90CfugT/3NoAAA"
        image2 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="

        # Create a profile with the first image
        self.chat.set_profile(display_name="TestUser", full_name="Test User", image=image1)
        profile = self.chat.get_profile()
        self.assertEqual(profile.image, image1, "Failed to set initial profile image.")

        # Update the profile image to the second image
        self.chat.update_profile(image=image2)
        profile = self.chat.get_profile() # we need to get this again
        self.assertEqual(profile.image, image2, "Failed to update profile image.")

if __name__ == "__main__":
    unittest.main()
