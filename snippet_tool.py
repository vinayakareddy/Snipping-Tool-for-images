import cv2
ref_point = []
crop = False

def shape_selection(event,x,y,flags,param):
    global ref_point, crop

    if event ==  cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x,y)]

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y))
        cv2.rectangle(image, ref_point[0], ref_point[1], (0,255,0), 2)
        cv2.imshow("image", image)


image = cv2.imread('dhoni.jpg')
clone =image.copy()

#mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', shape_selection) #shape_selection ->create refernce point


while True:
    cv2.imshow('image',image)
    key = cv2.waitKey(1) #waitkey 1 sec
  
 #r for reset of selection
    if key == ord('r'):
        image = clone.copy()
#crop the image
    elif key == ord('c'):
        break

if len(ref_point) == 2:
    crop_image = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow('crop_image',crop_image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
