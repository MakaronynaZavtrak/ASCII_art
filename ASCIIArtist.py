from PIL import Image
import settings
import os
import numpy as np

###Позволяет преобразовывать изображения в текстовые представления с возможностью их сохранения###
class ASCIIArtist:
    ###Обобщенный метод для получения масива пикселей из изображения###
    def prepare_image(self, image_path: str, width: int, height: int, color: bool = False):
            settings.logger.info(f"Opening image from: {image_path}")
            with Image.open(image_path) as image:
                if height is None:
                    height = int(settings.good_relation * (width / image.width) * image.height)
                settings.logger.info(f"Resizing image to width={width}, height={height}")
                image = image.resize((width, height))
            
            if color:
                image = image.convert('RGB')
                pixel_array = np.array(image)
            else:
                 image = image.convert('L')
                 pixel_array = np.array(image, dtype=np.int32)
            return pixel_array

    ###Из исходного изображения возвращает grayscale-строку###
    def convert_image_to_grayscale(self, image_path: str, width = settings.default_width, height = None) -> str:
            pixel_array = self.prepare_image(image_path, width, height, color=False)
            indices = (pixel_array * len(settings.ascii_chars) // settings.max_bright).astype(np.int32)
            ascii_chars_array = np.array(list(settings.ascii_chars))
            ascii_image_array = ascii_chars_array[indices]
            ascii_image = '\n'.join(''.join(row) for row in ascii_image_array)
            settings.logger.info("Successfully converted image to grayscale")
            return ascii_image
    
    ###Из исходного изображения возвращает ansii-строку###
    def convert_image_to_ansi(self, image_path: str, width = settings.default_width, height = None) -> str:
        pixel_array = self.prepare_image(image_path, width, height, color=True)

        brightness_array = pixel_array.astype(np.int32).mean(axis=2).astype(np.int32)
        indices = (brightness_array * len(settings.ascii_chars) // settings.max_bright).clip(0, len(settings.ascii_chars) - 1)
        ascii_chars_array = np.array(list(settings.ascii_chars))
        chars = ascii_chars_array[indices]
        r = pixel_array[:, :, 0]
        g = pixel_array[:, :, 1]
        b = pixel_array[:, :, 2]

        ansi_array = np.char.add(
             np.char.add(
                  np.char.add(
                       np.char.add(
                            np.char.add(
                                 "\033[38;2;",
                                 r.astype(str)
                            ),
                            ";" + g.astype(str)
                       ),
                       ";" + b.astype(str)
                  ),
                  "m" + chars
             ),
             "\033[0m"
        )

        lines = [''.join(row) for row in ansi_array]
        ascii_image = '\n'.join(lines)

        settings.logger.info("Succesfully converted image to ANSI")
        return ascii_image
        
    ###Загружает ascii-строку в текстовый файл###
    def upload_image(self, ascii_image: str, output_path: str):
        try:
            with open(output_path, "w") as file:
                file.write(ascii_image)
                settings.logger.info(f"Successfully saved ASCII-image to {output_path}")
        except FileNotFoundError as e:
                settings.logger.error(f"FileNotFoundError: {e}")
        except Exception as e:
                settings.logger.error(f"Unexpected error while saving: {e}")
    
    ###Обрабатывает логику исполнения программы###
    def run(self, image_path: str = None, output_path: str = None, width: int = settings.default_width, height = None):
        if not image_path:
            image_path = input("Enter a path to image.\n>>> ")

        image_path = os.path.abspath(os.path.expanduser(image_path.strip("'").strip('"')))
        if not os.path.isfile(image_path):
            settings.logger.error(f'File not found at: {image_path}')
            return

        is_satisfied_answer = False
        while not is_satisfied_answer: 
            user_answer = input("What type of ascii do you want? [C/c - Colourful] | [G/g - Grayscale]\n>>> ")
            match user_answer.upper():
                case 'C':
                    action = self.convert_image_to_ansi
                    break
                case 'G':
                    action = self.convert_image_to_grayscale
                    break
                case _:
                    settings.logger.info(f'Unexpected answer: {user_answer}')
            
        try:
            ascii_image = action(image_path, width, height)
        except Exception as e:
            settings.logger.exception("Error with converting image")
            return

        if not output_path:
            is_satisfied_answer = False
            while not is_satisfied_answer:
                user_answer = input("Do you want to save the result? [Y/y - Yes] | [N/n - No]\n>>> ")   
                match user_answer.upper():
                    case 'Y':
                        output_path = input('Enter a destination path.\n>>> ')
                        is_satisfied_answer = True
                    case 'N':
                        print(ascii_image)
                        return
                    case _:
                        settings.logger.warning('Unexpected answer:', user_answer)

        output_path = os.path.abspath(os.path.expanduser(output_path.strip('"').strip("'")))
        self.upload_image(ascii_image, output_path)