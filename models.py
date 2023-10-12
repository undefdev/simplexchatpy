from dataclasses import dataclass
from dataURI import DataURI

@dataclass
class Profile:
    displayName: str   # non-empty string without spaces, must not start with # or @ 
    fullName: str      # suprisingly not optional
    image: DataURI = None  # optional field

from dataclasses import dataclass

@dataclass
class MessageContent:
    type: str
    content: dict

    def __post_init__(self):
        if self.type not in ["text", "link", "image", "file"]:
            if "text" in self.content and self.content["text"] != "":
                self.content["from"] = self.type
                self.type = "text"  # default to text type
            else:
                raise ValueError("Unrecognized type without a valid text property.")

@dataclass
class TextContent(MessageContent):
    def __init__(self, text: str):
        if text == "":
            raise ValueError("The 'text' property cannot be an empty string.")
        super().__init__(type="text", content={"text": text})

@dataclass
class LinkContent(MessageContent):
    def __init__(self, text: str, preview: str = None):
        if text == "":
            raise ValueError("The 'text' property cannot be an empty string.")
        super().__init__(type="link", content={"text": text, "preview": preview})

@dataclass
class ImageContent(MessageContent):
    def __init__(self, text: str, image: str):
        if image == "":
            raise ValueError("The 'image' property cannot be empty.")
        super().__init__(type="image", content={"text": text, "image": DataURI(image)})

@dataclass
class FileContent(MessageContent):
    def __init__(self, text: str):
        super().__init__(type="file", content={"text": text})


@dataclass
class MessageContainer:
    content: MessageContent
    file: str = None  # placeholder for file invitations
    quote: str = None  # placeholder for quotes
    forward: bool = False  # placeholder for forward flag

    def __post_init__(self):
        if self.quote and self.forward:
            raise ValueError("A message cannot have both a quote and a forward flag.")
