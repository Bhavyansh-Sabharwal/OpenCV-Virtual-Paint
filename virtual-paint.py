import cv2
import numpy as np

# HSV color range for the object to track (blue)
lower_bound = (100, 100, 100)
upper_bound = (130, 255, 255)

# Initialize points for drawing
points = []

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a blank canvas
canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Mirror the frame horizontally
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the target color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Morphological operations to reduce noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Calculate the center of the contour
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            points.append((cx, cy))

    # Draw on the canvas
    for i in range(1, len(points)):
        if points[i - 1] is None or points[i] is None:
            continue
        cv2.line(canvas, points[i - 1], points[i], (255, 0, 0), 3)

    # Merge the canvas with the original frame
    combined = cv2.add(frame, canvas)
    
    # Create a white background for the mask display
    mask_canvas = np.zeros_like(canvas)
    mask_canvas.fill(255)
    
    # Draw the path on the mask canvas in black
    for i in range(1, len(points)):
        if points[i - 1] is None or points[i] is None:
            continue
        cv2.line(mask_canvas, points[i - 1], points[i], (0, 0, 0), 3)

    # Display the result
    cv2.imshow('Virtual Paint', combined)
    cv2.imshow('Mask', mask_canvas)

    # Clear canvas if 'c' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros_like(frame)
        points = []

    # Quit if 'q' is pressed
    elif key == ord('q'):
        # Save the canvas before quitting only if we have drawn something
        if len(points) > 0:
            cv2.imwrite('virtual_paint_output.png', canvas)
        break

# Release resources
cap.release()
cv2.destroyAllWindows()