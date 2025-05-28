from PIL import Image, ImageOps, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def load_input_image_as_np_array(file_name, crop_rect: (int, int, int, int), grayscale=True,
                                 contrast_enhance_factor=1.5):
    """
    :param file_name: The path to the input image file.
    :param crop_rect: The rectangle region to be cropped from the file; specified as a (x, y, w, h) tuple.
    :param grayscale: Whether or not the image is to be converted to grayscale.
    :param contrast_enhance_factor: The factor by which the image contrast is enhanced.
    :return:
    """

    im = Image.open(file_name)

    x, y, w, h = crop_rect
    im = im.crop((x, y, x + w, y + h))

    if grayscale:
        im = ImageOps.grayscale(im)

    if contrast_enhance_factor != 1:
        im = ImageEnhance.Contrast(im).enhance(contrast_enhance_factor)

    return np.array(im)


def show_scalar_field_plot(array: np.array, grayscale=True):
    if grayscale:
        # Create a custom colormap that goes from black to white
        colors = [(0, 0, 0), (1, 1, 1)]  # Black to white
        cmap_name = 'bw_cmap'
        bw_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=256)

        plt.imshow(array, cmap=bw_cmap)
    else:
        plt.imshow(array)

    plt.colorbar()
    plt.show()


def get_polygon_area(vertices):
    # Vertices is a list of (x,y) coordinate tuples in counterclockwise order.
    num_of_vertices = len(vertices)

    # Using shoelace formula
    area = 0

    for i in range(num_of_vertices):
        j = (i+1) % num_of_vertices
        area += vertices[i][0] * vertices[j][1] - vertices[i][1] * vertices[j][0]

    area /= 2

    return area


if __name__ == '__main__':
    print(get_polygon_area([(0, 0), (1, 0), (1,1), (0, 1)]))