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


def apply(image):
    bordered_image = border(image)

    watermarked_image = watermark(bordered_image)

    return watermarked_image


def get_next_image_index(file, files):
    index = files.index(file)
    if index > len(files):
        return 0
    return index-1


def transition_image(current_image, file, files):
    next_image = get_next_image(file, files)
    next_image_applied = apply(next_image)

    for alpha in range(1, 11):
        alpha = alpha/10.0
        beta = 1 - alpha
        cv2.imshow('showing_images', cv2.addWeighted(current_image, alpha, next_image_applied, beta, 0.1))
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()


def get_next_image(file, files):
    next_image_index = get_next_image_index(file, files)
    return load(files[next_image_index])


def display_images(files):
    for current_file in itertools.cycle(files):
        image = load(current_file)
        applied_image = apply(image)

        show(applied_image)

        transition_image(applied_image, current_file, files)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    files = get_files(repository)

    display_images(files)
