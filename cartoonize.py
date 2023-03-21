import cv2
import numpy as np

# Read the image and downscale it
img = cv2.imread('elon.png')

# Apply a simplified color quantization filter to the image
quantized = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
Z = quantized.reshape((-1,3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
_,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
quantized = res.reshape((quantized.shape))

# Apply a bilateral filter to the quantized image
filtered = cv2.bilateralFilter(quantized, 9, 75, 75)

# Apply a median blur to the filtered image
blurred = cv2.medianBlur(filtered, 9)

# Convert the blurred image to grayscale
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

# Apply an adaptive threshold to the grayscale image
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply the Canny edge detection algorithm to the thresholded image
edges = cv2.Canny(threshold, 100, 200)

# Dilate the edges to make them thicker
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(edges, kernel, iterations=2)

# Merge the edge-detected image with the original image using bitwise AND operator
cartoon = cv2.bitwise_and(img, img, mask=dilated)

# Convert the merged image to grayscale and invert it to create a black and white effect
bw_cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2GRAY)
bw_cartoon = cv2.bitwise_not(bw_cartoon)

# Apply a halftone effect to the black and white cartoonized image
height, width = bw_cartoon.shape
halftone = np.zeros((height, width, 3), np.uint8)
for i in range(height):
    for j in range(width):
        value = bw_cartoon[i, j]
        if value < 64:
            halftone[i, j] = (0, 0, 0)  # black
        elif value < 128:
            halftone[i, j] = (0, 0, 255)  # blue
        elif value < 192:
            halftone[i, j] = (0, 255, 0)  # green
        else:
            halftone[i, j] = (255, 255, 255)  # white

# Display the halftone cartoonized image
cv2.imshow('Halftone Cartoon', halftone)
cv2.waitKey(0)
cv2.destroyAllWindows()
