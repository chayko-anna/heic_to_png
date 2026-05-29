from PIL import Image
import pillow_heif
from pathlib import Path
import argparse
import logging

pillow_heif.register_heif_opener()

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def convert_img(input_dir: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    for heic_file in input_dir.glob("*.heic"):
        try:
            png_file = output_dir / (heic_file.stem + ".png")
            with Image.open(heic_file) as img:
                img.save(png_file, format="PNG", optimize=True)

            logging.info(f"{input_dir.name} to {png_file.name} - ok")

        except Exception as e:
            logging.error(f"Failed: {input_dir} ({e})")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input", type=Path, help="Input directory")
    parser.add_argument("output", type=Path, help="Output directory")

    args = parser.parse_args()

    if not args.input.exists():
        logging.error("Invalid input directory")
        return

    convert_img(input_dir=args.input, output_dir=args.output)


if __name__ == "__main__":
    main()
