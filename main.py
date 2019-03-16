import os
import cv2
import time
import itertools


def get_files(path):
    for _, _, files in os.walk(path):
        return files


def watermark_image(image):
    watermark = cv2.imread("watermark.png")

    watermark_height, watermark_width = watermark.shape[:2]
    image_height, image_width = image.shape[:2]

    image[
        image_height-watermark_height:image_height,
        image_width-watermark_width:image_width] = watermark

    return image


def display_images(repository, files):
    BLUE = [255, 0, 0]

    for file in itertools.cycle(files):
        img = cv2.imread(os.path.join(repository, file))
        bordered_image = cv2.copyMakeBorder(
            img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLUE)

        watermarked_image = watermark_image(bordered_image)
        
        cv2.imshow('img', watermarked_image)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    repository = f"{os.getcwd()}/images"

    files = get_files(repository)

    display_images(repository, files)
