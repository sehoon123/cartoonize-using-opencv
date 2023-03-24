import cv2

# Read the image and downscale it
img = cv2.imread('elon.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detection algorithm to the grayscale image
edges = cv2.Canny(gray, 100, 200)

# Dilate the edges to make them thicker
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
dilated = cv2.dilate(edges, kernel, iterations=2)

# Display the edge-detected image
cv2.imshow('Edges', dilated)
cv2.imwrite('cartoon_canny_like_v2.jpg', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
