import cv2
import numpy as np

img = cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# Log-magnitude spectrum
magnitude_spectrum = np.log1p(np.abs(fshift))

# Contrast stretching để dễ nhìn
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Lưu ra file để mở bằng Paint và tìm tọa độ
cv2.imwrite("test_view_images.png", magnitude_spectrum)
print('Lưu ảnh thành công')
def gaussian_notch_reject(shape, u_cen, v_cen, D0):
    M, N = shape
    H = np.ones((M, N))
    for u in range(M):
        for v in range(N):
            D1 = np.sqrt((u - u_cen)**2 + (v - v_cen)**2)
            D2 = np.sqrt((u + u_cen - M)**2 + (v + v_cen - N)**2)
            H[u, v] = 1 - np.exp(-0.5 * ((D1 * D2) / (D0**2))**2)
    return H