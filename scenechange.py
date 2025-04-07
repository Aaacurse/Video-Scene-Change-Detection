import cv2
import time
from datetime import timedelta

def detect_scene_changes(video_path, output_file="scene_changes.txt", verbose=True):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # fps = cap.get(cv2.CAP_PROP_FPS)
    
    success, frame = cap.read()
    if not success:
        print("Error: Unable to read the first frame.")
        cap.release()
        return
    
    previous_histogram = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    previous_histogram = cv2.normalize(src=previous_histogram, dst=previous_histogram).flatten()
    
    last_scene_change = 0
    current_frame = 0
    scene_changes = ["Scene changes timestamps:\n"]
    start_time = time.time()
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        current_frame += 1
        histogram = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        histogram = cv2.normalize(src=histogram, dst=histogram).flatten()
        
        similarity = cv2.compareHist(previous_histogram, histogram, cv2.HISTCMP_CORREL)
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        rounded_time=round(current_time,2)
        
        if similarity < 0.95 and (current_time - last_scene_change >= 1 or last_scene_change == 0):
            td = timedelta(seconds=rounded_time)
            total_seconds = td.total_seconds()
            minutes = int(total_seconds // 60)
            seconds = total_seconds % 60
            timestamp = f"0:00:{minutes:02}:{seconds:05.2f}"
            scene_changes.append(f"{timestamp}\n")
            last_scene_change = current_time
        
        if verbose and total_frames > 0:
            progress = int(50 * current_frame / total_frames)
            bar = "[" + "=" * progress + " " * (50 - progress) + "]"
            elapsed_time = time.time() - start_time
            fps_display = current_frame / elapsed_time if elapsed_time > 0 else 0
            print(f"\r{bar} {current_frame}/{total_frames} frames processed, FPS: {fps_display:.2f}", end="")
        
        previous_histogram = histogram
    
    cap.release()
    
    with open(output_file, "w") as f:
        f.writelines(scene_changes)
    
    print(f"\nScene changes saved to {output_file}")

# Example usage
# detect_scene_changes("angle.mp4")
