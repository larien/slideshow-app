import os
import cv2
import time
import itertools


def get_files(path):
    for _, _, files in os.walk(path):
        return files


def display_images(repository, files):
    for file in itertools.cycle(files):
        img = cv2.imread(os.path.join(repository, file))
        cv2.imshow('img', img)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    repository = f"{os.getcwd()}/images"

    files = get_files(repository)

    display_images(repository, files)
