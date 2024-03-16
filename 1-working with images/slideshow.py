import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("coca-cola-logo.png")
coke_img = cv2.imread("coca-cola-logo.png")

# # Use matplotlib imshow()
# plt.imshow(cb_img)
# plt.title("matplotlib imshow")
# plt.show()

# Use opencv imshow()
window1 = cv2.namedWindow("w1")
cv2.imshow(window1, cb_img)
cv2.waitKey(0)
cv2.destroyWindow(window1)

window4 = cv2.namedWindow("w4")

Alive = True
while Alive:
    cv2.imshow(window4, cb_img)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        Alive = False
cv2.destroyAllWindows(window4)
cv2.destroyAllWindows()
stop = 1
        