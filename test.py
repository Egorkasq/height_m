from flask import Flask, request
import cv2
import logging


class MyServer(Flask):
    # def __init__(self, *args, **kwargs):
    #     super(MyServer, self).__init__(*args, **kwargs)

    # @self.app.route('/load_image', methods=["GET"])
    def load_img(self):
        json_file = request.args
        path_to_img = json_file["image_path"]
        self.height_map = cv2.imread(path_to_img, 0)
        self.tile_size = (100, 100)

    def get_tile(self):

        json_file = request.args
        machine_loc = (int(json_file["machine_loc_x"]), int(json_file["machine_loc_y"]))
        logging.basicConfig(level=logging.INFO)

        tile_position = (machine_loc[0] - self.tile_size[0] // 2, machine_loc[1] - self.tile_size[1] // 2)  # top left coord

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