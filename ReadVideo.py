import cv2
video = cv2.VideoCapture("AnthonyShkraba.mp4")

if(video.isOpened() == False):
    print("Unable to read the feed")

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)

output = cv2.VideoWriter('Boxing.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while(True):
    ret, frame = video.read()
    cv2.imshow("Class 105 Webcam", frame)
    if cv2.waitKey(25) == 32:
        break
video.release()
output.release()
cv2.destroyAllWindows() 
