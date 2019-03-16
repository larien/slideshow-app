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


def watermark_image(image):
    watermark = cv2.imread(watermark_file)

    watermark_height, watermark_width = watermark.shape[:2]
    image_height, image_width = image.shape[:2]

    image[
        image_height-watermark_height:image_height,
        image_width-watermark_width:image_width] = watermark

    return image


def border_image(image):
    bordered_image = cv2.copyMakeBorder(
            image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=color)

    return bordered_image


def load_image(file):
    image = cv2.imread(os.path.join(repository, file))

    return image


def display_images(repository, files):

    for file in itertools.cycle(files):
        image = load_image(file)

        bordered_image = border_image(image)

        watermarked_image = watermark_image(bordered_image)

        cv2.imshow('img', watermarked_image)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":

    files = get_files(repository)

    display_images(repository, files)
