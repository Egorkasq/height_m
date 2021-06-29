from flask import Flask
from flask import request
import logging
import cv2
import copy

app = Flask(__name__)

HEIGHT_MAP = cv2.imread("./image/landshaft-bernskikh-alp-v-yasniy-den_thumb.jpg", 0)
TILE_SIZE = (100, 100)


@app.route("/get_tile", methods=["GET"])
def get_tile():
    json_file = request.args
    machine_loc = (int(json_file["x"]), int(json_file["y"]))

    tile_size = TILE_SIZE
    height_map = copy.copy(HEIGHT_MAP)

    logging.basicConfig(level=logging.INFO)

    tile_position = (
        machine_loc[0] - tile_size[0] // 2, machine_loc[1] - tile_size[1] // 2)  # top left coord

    new_position = list(tile_position)

    if tile_position[0] < 0 and tile_position[1] < 0:
        new_position[0] = 0
        new_position[1] = 0

        logging.info("top left of tile {}".format(new_position))
        tile = height_map[new_position[0]: new_position[0] + tile_size[0],
               new_position[1]: new_position[1] + tile_size[1]]
        return {"image": tile.tolist()}

    if tile_position[0] < 0:
        new_position[0] = 0

    if tile_position[1] < 0:
        new_position[1] = 0

    if tile_position[0] > height_map.shape[0] - tile_size[0] // 2 and \
            tile_position[1] > height_map.shape[1] - tile_size[1] // 2:
        new_position[0] = height_map.shape[0] - tile_size[0]
        new_position[1] = height_map.shape[1] - tile_size[1]

        logging.info("top left of tile {}".format(new_position))
        tile = height_map[new_position[0]: new_position[0] + tile_size[0] // 2,
               new_position[1]: new_position[1] + tile_size[1] // 2]

        return {"image": tile.tolist()}

    if tile_position[0] > height_map.shape[0] - tile_size[0]:
        new_position[0] = height_map.shape[0] - tile_size[0]

    if tile_position[1] > height_map.shape[1] - tile_size[1]:
        new_position[1] = height_map.shape[1] - tile_size[1]

    logging.info("top left of tile {}".format(new_position))

    tile = height_map[new_position[0]: new_position[0] + tile_size[0],
           new_position[1]: new_position[1] + tile_size[1]]

    # cv2.imwrite('')
    return {"image": tile.tolist()}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090)
