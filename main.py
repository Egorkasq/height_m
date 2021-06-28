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

    new_position = list(tile_position)

    if tile_position[0] < 0 and tile_position[1] < 0:

        new_position[0] = 0
        new_position[1] = 0

        logging.info("top left of tile {}".format(new_position))

        return height_map[new_position[0]: new_position[0] + tile_size[0],
                          new_position[1]: new_position[1] + tile_size[1]]

    if tile_position[0] < 0:
        new_position[0] = 0

    if tile_position[1] < 0:
        new_position[1] = 0

    if tile_position[0] > height_map.shape[0] - tile_size[0] // 2 and \
            tile_position[1] > height_map.shape[1] - tile_size[1] // 2:

        new_position[0] = height_map.shape[0] - tile_size[0]
        new_position[1] = height_map.shape[1] - tile_size[1]

        logging.info("top left of tile {}".format(new_position))

        return height_map[new_position[0]: new_position[0] + tile_size[0] // 2,
                          new_position[1]: new_position[1] + tile_size[1] // 2]

    if tile_position[0] > height_map.shape[0] - tile_size[0]:
        new_position[0] = height_map.shape[0] - tile_size[0]

    if tile_position[1] > height_map.shape[1] - tile_size[1]:
        new_position[1] = height_map.shape[1] - tile_size[1]

    logging.info("top left of tile {}".format(new_position))

    tile = height_map[new_position[0]: new_position[0] + tile_size[0],
                      new_position[1]: new_position[1] + tile_size[1]]

    return tile


if __name__ == '__main__':
    map_size_h = 100
    map_size_w = 100
    image = cv2.imread("landshaft-bernskikh-alp-v-yasniy-den_thumb.jpg", 0)
    # 800 450
    point_x = 300
    point_y = 300

    # computation_tile(image, (point_y, point_x))
    computation_tile(image, (point_y, point_x), (map_size_h, map_size_w))
