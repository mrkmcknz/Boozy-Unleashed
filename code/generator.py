import json
import os
import random

from PIL import Image


class BoozyGenerator:
    _traits = ["backgrounds", "bodies", "eyes", "head"]
    _supply = 200

    def generate_unleashed_boozy(self) -> dict:
        boozy = {"backgrounds": None, "bodies": None, "eyes": None, "head": None}
        for trait in self._traits:
            boozy[trait] = random.choice(os.listdir(f"art/{trait}"))

        return boozy

    def generate_unleased_boozy_metadata(self, boozy: dict, index: int):
        metadata = {
            "name": f"Boozy Unleashed #{index}",
            "image": f"ipfs:://CHANGEME/{index}.png",
            "attributes": [],
        }
        for trait in self._traits:
            metadata["attributes"].append(
                {
                    "trait_type": trait,
                    "trait_value": boozy[trait].replace(".png", ""),
                }
            )
        with open(f"output/metadata/{index}.json", "w") as outfile:
            json.dump(metadata, outfile)

    def generate_unleashed_boozy_image(self, boozy: dict, image_key: str):
        img = Image.new("RGBA", (2048, 2048), color="white")

        for trait in self._traits:
            trait_image = Image.open(f"art/{trait}/{boozy[trait]}").convert("RGBA")
            img = Image.alpha_composite(img, trait_image)
            trait_image.close()

        img.save(f"output/images/{image_key}.png")

    def generate_boozies(self, count: int):
        boozies = []
        while len(boozies) < count:
            boozy = self.generate_unleashed_boozy()
            if boozy not in boozies:
                boozies.append(boozy)

        for index, boozy in enumerate(boozies):
            self.generate_unleased_boozy_metadata(boozy, index)
            self.generate_unleashed_boozy_image(boozy, index)
