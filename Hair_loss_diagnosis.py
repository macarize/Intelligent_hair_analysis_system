import cv2
import numpy as np

def clustering(image, k) :
    pixel_values = image.reshape((-1, 1))
    pixel_values = np.float32(pixel_values)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.2)
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    image = segmented_image.reshape(image.shape)
    return image

path = "input_images/bald4_cropped.png"
width = 200
height = 200
errorV = np.array([])
image = cv2.imread(path, 0)
image = cv2.resize(image, dsize=(width, height), interpolation=cv2.INTER_AREA)
ret, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

kernel = np.ones((7,7),np.float32)/49
image = cv2.filter2D(image,-1,kernel)

image = clustering(image, 4)

kernel = np.ones((7,7),np.float32)/49
image = cv2.filter2D(image,-1,kernel)

image = clustering(image, 2)
image = cv2.bitwise_not(image)
ret, Midimage = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
ret, image = cv2.threshold(Midimage, 100, 3, cv2.THRESH_BINARY)

for i in range(1, 28):
    path = "Norwood-Hamilton/"
    path = path + str(i)
    path = path + ".png"
    model = cv2.imread(path, 0)
    model = cv2.resize(model, dsize=(width, height), interpolation=cv2.INTER_AREA)
    ret, model = cv2.threshold(model, 100, 3, cv2.THRESH_BINARY)

    error = image-model
    error = np.power(error, 2)
    error_sum = error.sum() / (width * height)
    errorV = np.append(errorV, error_sum)

k = 3
minIndex = np.argpartition(errorV, k)[:k]

print("3 promising status of hair")
for i in minIndex:
    print("Index : " + str(i+1) + " " + "MSE : " + str(errorV[i+1]))

cv2.imshow('Midimage', Midimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


