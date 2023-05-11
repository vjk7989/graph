import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
img = Image.open('pic.jpg')
# Convert the image to a numpy array
img_array = np.array(img)
# Perform the DWT transformation
coeffs = pywt.dwt2(img_array, 'haar')
cA, (cH, cV, cD) = coeffs
# Define the compression ratio
cr = 0.1

# Calculate the threshold
threshold = cr * np.max(np.abs(cH))

# Apply thresholding to the detail coefficients
cH_t = pywt.threshold(cH, threshold, 'soft')
cV_t = pywt.threshold(cV, threshold, 'soft')
cD_t = pywt.threshold(cD, threshold, 'soft')
# Reconstruct the compressed image
coeffs = cA, (cH_t, cV_t, cD_t)
img_compress = pywt.idwt2(coeffs, 'haar')

# Convert the numpy array to an image
img_compress = Image.fromarray(np.uint8(img_compress))
# Visualize the original and compressed images
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(img_compress, cmap='gray')
axes[1].set_title('Compressed Image')
axes[1].axis('off')
plt.tight_layout()
plt.show()
