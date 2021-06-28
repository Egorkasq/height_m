from flask import Flask
from flask import request
import logging
import cv2

app = Flask(__name__)


class MyServer(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height_map = cv2.imread(
            "/home/error/PycharmProjects/height_map/landshaft-bernskikh-alp-v-yasniy-den_thumb.jpg", 0)
        self.tile_size = (100, 100)

    @app.route("/get_tile", methods=["GET"])
    def get_tile(self):

        json_file = request.args
        machine_loc = (int(json_file["x"]), int(json_file["y"]))
        logging.basicConfig(level=logging.INFO)

        tile_position = (
        machine_loc[0] - self.tile_size[0] // 2, machine_loc[1] - self.tile_size[1] // 2)  # top left coord

        new_position = list(tile_position)

        if tile_position[0] < 0 and tile_position[1] < 0:
            new_position[0] = 0
            new_position[1] = 0

            logging.info("top left of tile {}".format(new_position))

            return self.height_map[new_position[0]: new_position[0] + self.tile_size[0],
                   new_position[1]: new_position[1] + self.tile_size[1]]

        if tile_position[0] < 0:
            new_position[0] = 0

        if tile_position[1] < 0:
            new_position[1] = 0

        if tile_position[0] > self.height_map.shape[0] - self.tile_size[0] // 2 and \
                tile_position[1] > self.height_map.shape[1] - self.tile_size[1] // 2:
            new_position[0] = self.height_map.shape[0] - self.tile_size[0]
            new_position[1] = self.height_map.shape[1] - self.tile_size[1]

            logging.info("top left of tile {}".format(new_position))

            return self.height_map[new_position[0]: new_position[0] + self.tile_size[0] // 2,
                   new_position[1]: new_position[1] + self.tile_size[1] // 2]

        if tile_position[0] > self.height_map.shape[0] - self.tile_size[0]:
            new_position[0] = self.height_map.shape[0] - self.tile_size[0]

        if tile_position[1] > self.height_map.shape[1] - self.tile_size[1]:
            new_position[1] = self.height_map.shape[1] - self.tile_size[1]

        logging.info("top left of tile {}".format(new_position))

        tile = self.height_map[new_position[0]: new_position[0] + self.tile_size[0],
               new_position[1]: new_position[1] + self.tile_size[1]]

        return tile


if __name__ == '__main__':
    temp = MapToTile
    temp.get_tile(10, 20)
    app.run(host="0.0.0.0", port=8090)
