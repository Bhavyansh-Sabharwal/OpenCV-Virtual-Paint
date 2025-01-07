# Virtual Paint

## Overview
Virtual Paint is a Python-based application that allows users to draw on a virtual canvas by moving a colored object (e.g., a blue marker cap) in front of a webcam. The program tracks the movement of the colored object in real-time and translates its path into strokes on the canvas. This is achieved using OpenCV for color detection, contour tracking, and image processing.

---

## Features
1. **Real-time Object Tracking**: Detects and tracks objects based on a specific HSV color range.
2. **Interactive Drawing**: Draws lines on a virtual canvas corresponding to the object's movement.
3. **Canvas Clearing**: Clear the canvas at any time by pressing `c`.
4. **Canvas Saving**: Save the current canvas as an image (`virtual_paint_output.png`) when exiting the application.
5. **Dynamic Mask Display**: Displays the path drawn on a separate mask for better visualization.

---

## Installation

1. **Prerequisites**
   - Python 3.x
   - OpenCV (`opencv-python`)
   - NumPy

2. **Install Required Libraries**:
   ```bash
   pip install opencv-python opencv-python-headless numpy
   ```

---

## How to Run
1. Save the provided script as `virtual_paint.py`.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python virtual_paint.py
   ```

---

## Controls
- **Draw**: Move a blue-colored object (or an object matching the specified HSV range) in front of the webcam.
- **Clear Canvas**: Press `c` to reset the canvas.
- **Quit and Save**: Press `q` to exit and save the current canvas as `virtual_paint_output.png`.

---

## Configuration
The script is configured to detect objects within a specific HSV range (blue by default):
```python
lower_bound = (100, 100, 100)  # Lower HSV bounds
upper_bound = (130, 255, 255)  # Upper HSV bounds
```
To track a different color, adjust the `lower_bound` and `upper_bound` values. Use the **Dynamic HSV Range Selector** script (described in the troubleshooting section below) to fine-tune these values for your object.

---

## Troubleshooting

1. **Object Not Detected**:
   - Ensure that the object is within the HSV range defined in `lower_bound` and `upper_bound`.
   - Check the lighting conditions to reduce glare or shadows.
   - Use a color calibration script to dynamically determine the HSV range for your object.

2. **Canvas Not Displaying Properly**:
   - Ensure that the webcam feed is mirrored correctly using `cv2.flip()`.
   - Verify that the `canvas` is initialized as a blank image of the same size as the webcam feed:
     ```python
     if canvas is None:
         canvas = np.zeros_like(frame)
     ```
---

## Outputs
1. **Mask Window**: Displays the drawn path on a white background for visualization.
2. **Virtual Paint Window**: Displays the live webcam feed overlaid with the virtual canvas.
3. **Saved Canvas**: On quitting (`q`), the canvas is saved as `virtual_paint_output.png` if there are any drawings.
