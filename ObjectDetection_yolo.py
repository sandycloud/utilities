import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8m.pt")

# Open the video file
#video_path = "/path/to/videoFile.mp4"
video_path ="/home/ubuntu/image-detect/yolotestvideo-2.MOV"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    ret, frame = cap.read()

	if ret:
      # Run YOLOv8 inference on the frame
      results = model(frame)

      # Visualize the results on the frame
      annotated_frame = results[0].plot()

      # Display the annotated frame
      cv2.imshow("YOLOv8 Inference", annotated_frame)

      # Exit when 'q' is pressed
      if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
	else:
      #break loop if end of video reached
      break

#release video capture object adn close diplay window 
cap.release()
cv2.destroyAllWindows()
