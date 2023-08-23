import tkinter as tk
import threading
from tkVideoPlayer import TkinterVideo

# Video paths
video1 = 'Ideal.mp4'
video2 = 'Speak.mp4'
video3 = 'Listen.mp4'

# Initiate player variable
video_player = None

def play_video(video_path):
    global video_player

    # If the player variable is not empty, stop the current video and delete the player
    if video_player:
        video_player.stop()
        video_player.pack_forget()

    video_player = TkinterVideo(root, scaled=True)
    video_player.load(r"{}".format(video_path))
    video_player.pack(expand=True, fill="both")
    video_player.play()

def play_videos():
    while True:
        play_video(video1)
        play_video(video2)
        play_video(video3)

# Create a GUI window
root = tk.Tk()
root.geometry("600x600")
root.title("Video Player")

# Start playing videos in a separate thread
video_thread = threading.Thread(target=play_videos)
video_thread.start()

root.mainloop()
