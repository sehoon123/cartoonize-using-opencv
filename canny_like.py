import cv2

# Read the image and downscale it
img = cv2.imread('image.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Apply a bilateral filter to the image
filtered = cv2.bilateralFilter(img, 9, 75, 75)

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

# Display the black and white cartoonized image
cv2.imshow('Black and White Cartoon', bw_cartoon)
cv2.imwrite('cartoon_canny_like_v1.jpg', bw_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
