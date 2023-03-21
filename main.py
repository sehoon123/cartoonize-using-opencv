import cv2

# Read the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a bilateral filter to the grayscale image
bilateral = cv2.bilateralFilter(gray, 9, 75, 75)

# Apply an adaptive threshold to the bilateral-filtered image
threshold = cv2.adaptiveThreshold(bilateral, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Convert the binary image back to color
color = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)

# Merge the cartoonized image with the original image
cartoon = cv2.bitwise_and(img, color)

# Display the cartoonized image
cv2.imshow('Cartoon', cartoon)
cv2.imwrite('cartoon_fixed.jpg', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
