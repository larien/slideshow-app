import os
import cv2
import time
import itertools


def get_files(path):
    for _, _, files in os.walk(path):
        return files


def display_images(repository, files):
    BLUE = [255, 0, 0]

    for file in itertools.cycle(files):
        img = cv2.imread(os.path.join(repository, file))
        bordered_img = cv2.copyMakeBorder(
            img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLUE)
        watermark = cv2.imread("watermark.png")
        watermark_height, watermark_width = watermark.shape[:2]
        img_height, img_width = img.shape[:2]
        bordered_img[img_height-watermark_height:img_height, img_width-watermark_width:img_width] = watermark
        cv2.imshow('img', bordered_img)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    repository = f"{os.getcwd()}/images"

    files = get_files(repository)

    display_images(repository, files)
