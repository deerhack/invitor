from PIL import Image, ImageDraw, ImageFont
from person import Person


class InviteGenerator:
    def __init__(
        self,
        image_path: str,
    ) -> None:
        self.image_path = image_path
        self.positions = []
        self.font = "./fonts/CabinetGrotesk-Medium.ttf"

    def create(
        self,
        person: Person,
    ) -> None:
        full_name = f"{person.first_name} {person.last_name}".title()
        with Image.open(self.image_path).convert("RGBA") as base:  # type:ignore
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            font = ImageFont.truetype(self.font, 80)  # type:ignore
            d = ImageDraw.Draw(txt)  # type:ignore

            y_factor = base.size[1] / 2 - 8 / 100 * base.size[1] / 2

            x_factor_dynamic = (1 - len(full_name) / 27) * base.size[0] / 2 + len(
                full_name
            )

            d.text(  # type:ignore
                (x_factor_dynamic, y_factor),
                full_name,
                font=font,
                fill=(255, 255, 255, 255),
            )
            #    d.text((10, 60), "World", font=font, fill=(255, 255, 255, 255))
            out = Image.alpha_composite(base, txt)
            # out.show()
            out.save(f"output/{person.first_name}_{person.last_name}.png", "png")  # type:ignore
            print(f"Saved {full_name}.png")
