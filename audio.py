from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Use the function
extract_audio('video1.mp4', 'extracted-python.mp3')