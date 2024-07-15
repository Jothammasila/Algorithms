img_url = "/home/jothammasila/Downloads/jkuat-main.jpg"

import skimage as ski
print(ski.__version__)

camera = ski.data.camera()
print(type(camera))


print(camera.size, camera.shape)
print(camera)

print(camera[10,20])
