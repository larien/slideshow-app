import os
import cv2
import time


def get_files(path):
    for _, _, files in os.walk(path):
        return files


def display_images(repository, files):
    i = 0
    while True:

        img = cv2.imread(os.path.join(repository, files[i]))
        print(f"Printing {files[i]}")
        cv2.imshow('img', img)
        time.sleep(2)
        i = i + 1
        if i == len(files):
            i = 0
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    repository = f"{os.getcwd()}/images"

    files = get_files(repository)

    display_images(repository, files)
