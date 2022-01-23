from PIL import Image

import cv2
import numpy as np

size = 80
images = [
    cv2.resize(cv2.imread("images/R_img1.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img2.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img3.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img4.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img5.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img6.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img7.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img8.png"), (size, size))]


def draw_sequence(width, height, data):
    collage = []
    for j in range(0, height):
        collage_line = []

        for i in range(j*width,(j+1)* width):
            collage_line.append(images[data[i]])

        collage.append(np.hstack(collage_line))

    out_data = np.vstack(collage)
    show_sequence(out_data)

def show_sequence(out_data):
    cv2.imshow("Final Collage", out_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_sequence(8,8,[2,2,2,2,2,4,2,2,
                   2,4,5,2,2,7,4,2,
                   2,3,3,2,2,2,3,2,
                   2,7,6,2,2,2,3,2,
                   2,5,3,3,3,3,3,2,
                   2,3,1,3,0,2,3,2,
                   2,7,3,3,3,3,6,2,
                   2,2,1,2,2,1,2,2])
