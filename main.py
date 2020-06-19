import cv2

src = cv2.imread('data/before/7.jpg',cv2.IMREAD_COLOR)

(B, G, R) = cv2.split(src)

dstB = cv2.equalizeHist(B)
dstG = cv2.equalizeHist(G)
dstR = cv2.equalizeHist(R)

merged = cv2.merge([dstB, dstG, dstR])

resize_merged = cv2.resize(merged, dsize=(640, 480), interpolation=cv2.INTER_AREA)
resize_src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)

cv2.imshow("Merged", resize_merged )
cv2.imshow('src', resize_src)
cv2.waitKey()
