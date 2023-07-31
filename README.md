## Attendance Tracking with Face Recognition

This Python script utilizes face recognition to perform real-time attendance tracking from a webcam video feed. It detects faces, compares them with known faces, and saves the recognized names along with timestamps to a CSV file.

### Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.6 or higher)
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)
- dlib (`dlib` package)
- face-recognition (`face-recognition` package)

You can install the required packages using the following command:

```bash
pip install opencv-python numpy dlib face-recognition
```

### Instructions

1. **Clone the Repository**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/your-username/your-repo.git
     ```
   - Alternatively, you can manually download the script file `attendance_face_recognition.py` from this repository.

2. **Prepare the Known Faces**
   - Create a directory named "known" and place images of the known individuals whose attendance you want to track. Each image should contain one person's face, and the image file name should match the person's name (without the file extension).
   - For example, you should have images like `known/john.jpg`, `known/emma.png`, etc.

3. **Update the Script**
   - Open the Python script file `attendance_face_recognition.py` in a text editor.
   - Replace the variable `known_images_dir` with the path to the "known" directory containing your known faces' images.

4. **Run the Script**
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script `attendance_face_recognition.py`.
   - Run the script using the following command:
     ```bash
     python attendance_face_recognition.py
     ```

5. **Perform Attendance Tracking**
   - The script will use your computer's webcam to capture video frames.
   - It will detect faces and compare them with the known faces.
   - When recognized, the person's name will be displayed on the video feed along with a rectangle around their face.
   - If the person is recognized for a duration of `attendance_duration` seconds (default: 7 seconds), their name and timestamp will be saved to a CSV file named `attendance.csv`.

6. **Exit the Script**
   - To stop the script and end attendance tracking, press the 'q' key on your keyboard.

### Attendance Report

Once you have run the script and captured attendance data in the `attendance.csv` file, you can access the data by reading the CSV file. You can use your preferred method or programming language to analyze and generate reports based on the collected attendance data.

### Important Notes

- Ensure that you have the necessary packages installed as mentioned in the "Prerequisites" section.
- Make sure your webcam is working correctly and accessible by the script.
- Provide sufficient lighting and clear images for accurate face recognition.
- The script automatically saves recognized names and timestamps to `attendance.csv`. However, you can modify the script to save the data to a different file or in a different format if needed.

By following these instructions, you can use the `attendance_face_recognition.py` script to perform face recognition-based attendance tracking and customize it to suit your specific needs.
