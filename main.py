import os
import cv2
import time
import itertools

repository = f"{os.getcwd()}/images"
watermark_file = "watermark.png"
color = [255, 0, 0]  # blue


def get_files(path):
    for _, _, files in os.walk(path):
        return files


def watermark(image):
    watermark = cv2.imread(watermark_file)

    watermark_height, watermark_width = watermark.shape[:2]
    image_height, image_width = image.shape[:2]

    image[
        image_height-watermark_height:image_height,
        0:watermark_width] = watermark

    return image


def border(image):
    bordered_image = cv2.copyMakeBorder(
            image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=color)

    return bordered_image


def load(file):
    image = cv2.imread(os.path.join(repository, file))

    return image


def show(image):
    cv2.imshow('showing_images', image)
    time.sleep(2)


def display_images(files):
    for file in itertools.cycle(files):
        image = load(file)

        bordered_image = border(image)

        watermarked_image = watermark(bordered_image)

        show(watermarked_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    files = get_files(repository)

    display_images(files)
