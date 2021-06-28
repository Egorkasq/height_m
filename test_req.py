import requests
#
req = requests.get("http://0.0.0.0:8090/load_image?image_path=/home/error/PycharmProjects/height_map/landshaft-bernskikh-alp-v-yasniy-den_thumb.jpg")
print(req.status_code)

# req = requests.get("http://0.0.0.0:8090/get_tile?x=100,y=100")
# print(req.status_code)