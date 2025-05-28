from Funcs import *
from Lens import Lens
import numpy as np


def compute_lens_grid():
    # Scalar field representing brightness values of the target image
    target_image_brightnesses = load_input_image_as_np_array("UncroppedImage.jpg", crop_rect=(650, 60, 1024, 1024))
    image_width, image_height = target_image_brightnesses.shape

    brightness_total = np.sum(target_image_brightnesses)

    target_image_brightnesses = np.divide(target_image_brightnesses, brightness_total)

    # show_scalar_field_plot(target_image_brightnesses)

    lens = Lens((image_width, image_height))


if __name__ == '__main__':
    compute_lens_grid()

