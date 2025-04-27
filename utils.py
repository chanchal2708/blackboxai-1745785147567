def load_audio_file(file_path, sr=22050):
    """
    Load an audio file.

    Parameters:
    - file_path: str, path to audio file
    - sr: int, sample rate

    Returns:
    - audio_data: np.ndarray, audio time series
    """
    import librosa
    audio_data, _ = librosa.load(file_path, sr=sr)
    return audio_data

def load_video_frames(video_path):
    """
    Load video frames from a video file.

    Parameters:
    - video_path: str, path to video file

    Returns:
    - frames: list of np.ndarray, video frames
    """
    import cv2
    frames = []
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames
