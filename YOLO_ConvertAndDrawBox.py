import numpy as np
import cv2
from typing import Tuple, List, Union

def denormalize_yolo_coordinates(
    image: np.ndarray, 
    norm_coord: Tuple[float, float, float, float]
    
) -> Tuple[float, float, float, float]:
    
    height, width, channels = image.shape
    x_center, y_center, w, h = float(norm_coord[0])*width, float(norm_coord[1])*height, float(norm_coord[2])*width, float(norm_coord[3])*height
    x1 = round(x_center-w/2)
    y1 = round(y_center-h/2)
    x2 = round(x_center+w/2)
    y2 = round(y_center+h/2)
    return x1, y1, x2, y2


def luma(color: Tuple[int, int, int]) -> float:  # weighted sum of RGB color [0, 1]
    return (0.212*color[0] + 0.701*color[1] + 0.087*color[0]) / 255


def dynamic_text_color(  # text color will change depending on the bounding box color [white, black]
    txt_color: Tuple[int, int, int]
) -> Tuple[int, int, int]:

    if luma(txt_color) > 0.5:
        return (0, 0, 0)
    else:
        return (255, 255, 255) 
    

def draw_text_box(
    image: np.ndarray,
    text: str,
    x: int,
    y: int,
    font: int,
    font_size: float,
    background_color: Tuple[int, int, int],
    thickness: int = 1,
) -> np.ndarray:
    
    text_color = dynamic_text_color(background_color)
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_size, thickness)
    text_left_offset = 7

    image = cv2.rectangle(image, (x, y), (x + text_width + text_left_offset, y - text_height - int(15 * font_size)), background_color, -1)
    image = cv2.putText(image, text, (x + text_left_offset, y - int(10 * font_size)), font, font_size, text_color, thickness, lineType=cv2.LINE_AA)
    return image


def draw_bbox(
    image: np.ndarray,
    title: str,
    color: Tuple[int, int, int],
    box_thickness: int,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
) -> np.ndarray:
    
    overlay = image.copy()
    overlay = cv2.rectangle(overlay, (x1, y1), (x2, y2), color, box_thickness)

    # dynamic adaptation of the font size based on the bounding box
    font_size = 0.25 + 0.07 * min(overlay.shape[:2]) / 100
    font_size = max(font_size, 0.5)
    font_size = min(font_size, 0.8)

    overlay = draw_text_box(image=overlay, text=title, x=x1, y=y1, font=2, font_size=font_size, background_color=color, thickness=1)

    return cv2.addWeighted(overlay, 0.75, image, 0.25, 0)


if __name__ == "__main__":
    img = cv2.imread("test_images/Motorcycle.jpg")
    
    ###################### Using list of normalized coordinates################################
    # norm_coord = [0.588137, 0.705081, 0.586461, 0.589839]
    # x1, y1, x2, y2 = denormalize_yolo_coordinates(img, norm_coord)
    # final_img = draw_bbox(img, "Cycle", (12, 255, 45), 2, x1, y1, x2, y2)
    # cv2.imshow('img', final_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    ##################### using the string of normalized coordinates ##########################
    norm_coord = open("test_images/Motorcycle.txt").read().strip().split(" ")[1:]  # reading the coordinates from the txt file generated after annotating
    x1, y1, x2, y2 = denormalize_yolo_coordinates(img, norm_coord)
    final_img = draw_bbox(img, "Bike", (255, 0, 0), 2, x1, y1, x2, y2)
    cv2.imshow('img', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
