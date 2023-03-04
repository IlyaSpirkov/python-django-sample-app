import os
from rest_framework.exceptions import ValidationError

MAX_SIZE = 10 * 1024 * 1024
VALID_EXTENSIONS = [".jpg", ".jpeg", ".png"]


def validate_image(image):
    ext = os.path.splitext(image.name)[1]
    if ext not in VALID_EXTENSIONS:
        raise ValidationError("Not valid file extension. Supported only .jpeg, .jpg, .png")
    if image.size > MAX_SIZE:
        raise ValidationError("File size must be less than 10Mb")
