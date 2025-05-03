import os
import unittest

import numpy as np
from PIL import Image

from ASCIIArtist import ASCIIArtist


class TestASCIIArtist(unittest.TestCase):
    def setUp(self):
        # Создает экземпляр ASCIIArtist и тестовое изображение
        self.artist = ASCIIArtist()
        self.test_image_path = "test_image.png"
        self.test_output_path = "test_output.txt"
        # Создает тестовое белое изображение 100x100 пикселей
        test_image = Image.new('RGB', (100, 100), color='white')
        test_image.save(self.test_image_path)

    def tearDown(self):
        # Удаляет тестовые файлы после выполнения тестов
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def test_prepare_image(self):
        # Проверяет преобразование в черно-белое изображение
        # Проверяет правильность размеров и типа выходных данных
        pixel_array = self.artist.prepare_image(self.test_image_path, 50, 50, color=False)
        self.assertIsInstance(pixel_array, np.ndarray)
        self.assertEqual(pixel_array.shape, (50, 50))

        # Проверяет преобразование в цветное изображение
        # Проверяет правильность размеров и типа выходных данных
        pixel_array = self.artist.prepare_image(self.test_image_path, 50, 50, color=True)
        self.assertIsInstance(pixel_array, np.ndarray)
        self.assertEqual(pixel_array.shape, (50, 50, 3))

    def test_convert_image_to_grayscale(self):
        # Проверяет конвертацию изображения в ASCII-строку
        # Проверяет, что результат не пустой и содержит переносы строк
        ascii_image = self.artist.convert_image_to_grayscale(self.test_image_path, 50, 50)
        self.assertIsInstance(ascii_image, str)
        self.assertTrue(len(ascii_image) > 0)
        self.assertIn('\n', ascii_image)

    def test_convert_image_to_ansi(self):
        # Проверяет конвертацию изображения в ANSI-строку с цветами
        # Проверяет наличие ANSI-последовательностей в результате
        ansi_image = self.artist.convert_image_to_ansi(self.test_image_path, 50, 50)
        self.assertIsInstance(ansi_image, str)
        self.assertTrue(len(ansi_image) > 0)
        self.assertIn('\033[', ansi_image)

    def test_upload_image(self):
        # Проверяет сохранение ASCII-арта в файл
        # Проверяет, что содержимое файла соответствует ожидаемому
        test_content = "Test ASCII art"
        self.artist.upload_image(test_content, self.test_output_path)
        self.assertTrue(os.path.exists(self.test_output_path))
        with open(self.test_output_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, test_content)


if __name__ == '__main__':
    unittest.main()
