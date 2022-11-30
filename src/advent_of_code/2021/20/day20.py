from io import StringIO
import numpy as np


def read_input(f):
    with open(f) as file:
        content = file.read()

    algorithm, image = content.split('\n\n')

    def to_bin(a):
        a = a.replace('.', '0')
        a = a.replace('#', '1')
        return a

    algorithm = to_bin(algorithm).strip()
    image = StringIO(to_bin(image))

    image = np.genfromtxt(image, delimiter=1, dtype=int)
    return algorithm, image


def apply_algorithm_n_times(algorithm, image, n=2):
    pad_value = 0
    for i in range(n):
        print(f'{i:02d}/{n}')
        image = np.pad(image, 3, constant_values=pad_value)
        enh_image = np.full_like(image, pad_value)
        row_count, column_count = image.shape
        for row in range(1, row_count - 1):
            for column in range(1, column_count - 1):
                region = image[row-1:row+2, column-1:column+2]
                bin_number = ''.join([str(i) for i in region.flatten()])
                dec_number = int(bin_number, 2)
                enh_value = int(algorithm[dec_number])
                enh_image[row, column] = enh_value

        # crop borders
        enh_image = enh_image[1:-1, 1:-1]
        pad_value = enh_image[0, 0]
        image = enh_image
    return image


def bright_spots(image):
    return image.sum()


if __name__ == '__main__':
    algorithm, image = read_input('input.txt')
    n_runs = 50
    image = apply_algorithm_n_times(algorithm, image, n=n_runs)
    n_bright = bright_spots(image)
    print(f'Number of bright spots after {n_runs} runs: {n_bright}')
