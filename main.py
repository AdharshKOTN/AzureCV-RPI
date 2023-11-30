import cv2
import time

def capture_image():
    # Open a connection to the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a frame from the camera
    ret, frame = cap.read()

    # Generate a filename based on the current timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"captured_image_{timestamp}.jpg"

    # Save the captured image
    cv2.imwrite(filename, frame)
    print(f"Image captured and saved as {filename}")

    # Release the camera
    cap.release()

if __name__ == "__main__":
    # Set the interval for capturing images (in seconds)
    capture_interval = 300  # 5 minutes

    try:
        while True:
            # Capture an image
            capture_image()

            # Wait for the specified interval before capturing the next image
            print(f"Waiting for {capture_interval} seconds before capturing the next image...")
            time.sleep(capture_interval)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to exit the loop gracefully
        print("Image capturing stopped.")
