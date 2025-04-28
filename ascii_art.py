from ASCIIArtist import ASCIIArtist
import argparse
import settings

def main():
    parser = argparse.ArgumentParser(description="Convert image to ASCII art")
    parser.add_argument('input', nargs='?', help='Path to the input image')
    parser.add_argument('output', nargs='?', help='Path to save ASCII-image (optional)')

    parser.add_argument('--input', dest='input_kw', help='Path to the input image')
    parser.add_argument('--output', dest='output_kw', help='Path to save ASCII-image (optional)')
    parser.add_argument('--width', dest='width_kw', type=int, help=f'Width of ASCII-image (default: {settings.default_width})')
    parser.add_argument('--height', dest='height_kw', type=int, help=f'Height of ASCII-image (default: width * {settings.good_relation})')

    args = parser.parse_args()
    image_path = args.input_kw or args.input
    output_path = args.output_kw or args.output
    width = args.width_kw or settings.default_width
    height = args.height_kw or None

    artist = ASCIIArtist()
    artist.run(image_path, output_path, width, height)

if __name__ == '__main__':
    main()