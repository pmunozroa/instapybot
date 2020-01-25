from config import get_image, get_dimensions, upload_image, tmp_img_path, upload_img_path
import cv2 as cv
import os
from PIL import Image as Img
from resizeimage import resizeimage as rImg

with open(tmp_img_path, 'wb') as image:
    image.write(get_image())
    img = cv.imread(tmp_img_path, cv.IMREAD_UNCHANGED)
    height = img.shape[0]
    width = img.shape[1]
    dimensions = get_dimensions(height, width)
with Img.open(tmp_img_path) as tmpimg:
    to_upload = rImg.resize_contain(tmpimg, dimensions)
    to_upload.save(upload_img_path, tmpimg.format)
    upload_image()
os.remove(upload_img_path)
os.remove(tmp_img_path)
