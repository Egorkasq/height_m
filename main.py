import cv2
import logging


def computation_tile(height_map, machine_loc, tile_size=(50, 50)):
    """

    :param height_map: np array
    :param machine_loc: loc of machine in (y, x) format
    :param tile_size: tile size
    :return: tile include machine
    """

    logging.basicConfig(level=logging.INFO)

    tile_position = (machine_loc[0] - tile_size[0] // 2, machine_loc[1] - tile_size[1] // 2)  # top left coord

    if tile_position[0] < 0 or tile_position[1] < 0:

        # correct tile position if machine near end of map
        delta_y = 0 - tile_position[0]
        delta_x = 0 - tile_position[1]
        correct_pos = (tile_position[0] + delta_y, tile_position[1] + delta_x)

        tile = height_map[correct_pos[0]: correct_pos[0] + tile_size[0],
                          correct_pos[1]: correct_pos[1] + tile_size[1], ]

        logging.info("Top left of tile {}".format(correct_pos))

    else:
        tile = height_map[tile_position[0]: tile_position[0] + tile_size[0],
                          tile_position[1]: tile_position[1] + tile_size[1], ]

        logging.info("top left of tile {}".format(tile_position))

    return tile


if __name__ == '__main__':
    map_size_h = 50
    map_size_w = 50
    image = cv2.imread("Heightmap.png", 0)

    point_x = 100
    point_y = 100

    computation_tile(image, (point_y, point_x))