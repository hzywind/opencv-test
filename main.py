import cv2

# Open the video file
cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

# Get the frames per second (fps) of the video
fps = cap1.get(cv2.CAP_PROP_FPS)

# Calculate the number of frames to capture for 10 seconds
frames_to_capture = 2 * fps

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out1 = cv2.VideoWriter('cliped-python.avi', fourcc, fps, (int(cap1.get(3)), int(cap1.get(4))))
out2 = cv2.VideoWriter('merged-python.avi', fourcc, fps, (int(cap1.get(3)), int(cap1.get(4))))

frame_count = 0
while(cap1.isOpened()):
    ret, frame = cap1.read()
    if ret==True:
        frame_count += 1
        if frame_count <= frames_to_capture:
            out1.write(frame)
        out2.write(frame)
    else:
        break

while(cap2.isOpened()):
    ret, frame = cap2.read()
    if ret==True:
        out2.write(frame)
    else:
        break

# Release everything when done
cap1.release()
cap2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()