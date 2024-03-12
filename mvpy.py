from moviepy.editor import VideoFileClip, concatenate_videoclips

# Open the video files
clip1 = VideoFileClip('video1.mp4')
clip2 = VideoFileClip('video2.mp4')

# Clip the first 2 seconds of each video
clip3 = clip1.subclip(0, 2)

# Write the first clipped video to a file
clip3.write_videofile('cliped-python.mp4')

# Concatenate the two clips and write the result to a file
final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile('merged-python.mp4')