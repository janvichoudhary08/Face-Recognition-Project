import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Try using DirectShow as discussed earlier

if not video.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release the video capture object and close the window properly
video.release()
cv2.destroyAllWindows()
