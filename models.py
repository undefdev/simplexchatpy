from dataclasses import dataclass
from dataURI import DataURI

@dataclass
class Profile:
    displayName: str   # non-empty string without spaces, must not start with # or @ 
    fullName: str      # suprisingly not optional
    image: DataURI = None  # optional field

@dataclass
class MessageContent:
    type: str
    content: str  # placeholder for actual content based on the type

@dataclass
class MessageContainer:
    content: MessageContent
    file: str = None  # placeholder for file invitations
    quote: str = None  # placeholder for quotes
    forward: bool = False  # placeholder for forward flag

