from utils import encode_message, decode_message
from models import Profile
import base64
import os

class SimplexChat:
    def __init__(self):
        # Mock message store for the sake of this implementation
        self.mock_message_store = []
        # Mock profile store
        self.profile = None
   
    def send_message(self, message_content):
        """Send a message using the SimpleX Chat Protocol."""
        encoded_message = encode_message(message_content)
        # Simulate sending the message by storing it in the mock message store
        self.mock_message_store.append(encoded_message)
        print("Message sent:", encoded_message)
    
    def receive_message(self):
        """Receive a message using the SimpleX Chat Protocol."""
        # Simulate receiving a message by retrieving the last message from the mock message store
        if not self.mock_message_store:
            print("No messages available")
            return None
        encoded_message = self.mock_message_store.pop()
        decoded_message = decode_message(encoded_message)
        return decoded_message

    def get_profile(self):
        """Retrieve the user's profile."""
        if not self.profile:
            print("Profile not set.")
            return None
        return self.profile

    @staticmethod
    def validate_display_name(display_name):
        """Helper method to validate the display name based on the protocol's constraints."""
        if not display_name or " " in display_name or display_name[0] in ["#", "@"]:
            raise ValueError("Invalid display name. Must be non-empty string without spaces and must not start with # or @")
        return display_name

    def set_profile(self, display_name, full_name, image=None):
        """Set the user's profile and send an x.info message."""
        display_name = self.validate_display_name(display_name)
        self.profile = Profile(displayName=display_name, fullName=full_name, image=image)
        print(f"Profile set for {display_name}")
        # send x.info message
        self.send_message(f"x.info: {self.profile}")

    def update_profile(self, display_name=None, full_name=None, image=None):
        """Update specific fields in the user's profile."""
        if not self.profile:
            raise ValueError("Profile not set. Use set_profile first.")
        if display_name:
            display_name = self.validate_display_name(display_name)
            self.profile.displayName = display_name
        if full_name:
            self.profile.fullName = full_name
        if image:
            self.profile.image = image
        print(f"Profile updated for {self.profile.displayName}")
        # send x.info message
        self.send_message(f"x.info: {self.profile}")

    def delete_profile(self):
        """Delete the user's profile."""
        if not self.profile:
            raise ValueError("No profile to delete.")
        self.profile = None
        print("Profile deleted.")


    def generate_probe(self):
        """Generate a random base64url-encoded 32 bytes probe."""
        random_bytes = os.urandom(32)
        probe = base64.urlsafe_b64encode(random_bytes).decode('utf-8')
        return probe

    def send_probe(self, contact):
        """Send a probe to a new contact or group member."""
        probe = self.generate_probe()
        # Store the probe with the contact for later validation 
        # (in a real-world scenario, you'd use a database or persistent storage)
        self.probes[contact] = probe
        self.send_message(f"x.info.probe: {probe}")

    def handle_received_probe(self, probe, sender_contact):
        """Handle the reception of a probe."""
        # Check if the probe matches any existing contact's profile (simplified for this mock implementation)
        for contact, stored_probe in self.probes.items():
            if stored_probe == probe:
                # Send back the probe hash via x.info.probe.check if a match is found
                self.send_message(f"x.info.probe.check: {hash(probe)}", recipient=sender_contact)
                return
        print(f"No matching profile found for probe from {sender_contact}")

    def handle_probe_confirmation(self, probe, sender_contact):
        """Handle the reception of an x.info.probe.ok message and merge contacts if required."""
        # Check if the received probe matches the one we sent (simplified for this mock implementation)
        if self.probes.get(sender_contact) == probe:
            # Merge the contacts (implementation would depend on your contact storage structure)
            print(f"Merged contact: {sender_contact}")
        else:
            print(f"Probe mismatch for contact: {sender_contact}")
