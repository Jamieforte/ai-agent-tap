from dataclasses import dataclass
from typing import List
from PIL import Image, ImageDraw
import io, os

@dataclass
class ProviderConfig:
    name: str
    env_keys: list[str]

class ImageProvider:
    name = "Placeholder"
    config = ProviderConfig(name="Placeholder", env_keys=[])

    def generate_image_bytes(self, prompt: str) -> bytes:
        # fallback placeholder: simple generated image
        img = Image.new("RGB", (768, 512), (240, 240, 240))
        d = ImageDraw.Draw(img)
        text = (prompt[:120] + "...") if len(prompt) > 120 else prompt
        d.text((20, 20), f"Provider: {self.name}\n{text}", fill=(0,0,0))
        b = io.BytesIO()
        img.save(b, format="PNG")
        return b.getvalue()

class OpenAIProvider(ImageProvider):
    name = "OpenAI (stub)"
    config = ProviderConfig(name=name, env_keys=["OPENAI_API_KEY"])

    def generate_image_bytes(self, prompt: str) -> bytes:
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            return super().generate_image_bytes(prompt)
        # TODO: 실제 OpenAI Images API 호출 구현
        return super().generate_image_bytes("OpenAI call (stub): " + prompt)

class PromeProvider(ImageProvider):
    name = "Prome (stub)"
    config = ProviderConfig(name=name, env_keys=["PROME_API_KEY"])

class MidjourneyProvider(ImageProvider):
    name = "Midjourney (stub)"
    config = ProviderConfig(name=name, env_keys=["MIDJOURNEY_TOKEN"])

def get_provider_names() -> List[str]:
    return [OpenAIProvider.name, PromeProvider.name, MidjourneyProvider.name, ImageProvider.name]

def get_provider(name: str):
    mapping = {
        OpenAIProvider.name: OpenAIProvider(),
        PromeProvider.name: PromeProvider(),
        MidjourneyProvider.name: MidjourneyProvider(),
        ImageProvider.name: ImageProvider(),
    }
    return mapping.get(name, ImageProvider())
