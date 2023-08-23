import tkinter as tk
from tkVideoPlayer import TkinterVideo

# Video paths
video1 = 'Ideal.mp4'
video2 = 'Speak.mp4'
video3 = 'Listen.mp4'

# Create a global variable to store the current video player
current_player = None

def play_video(video_path):
    global current_player

    # Stop the previously played video
    if current_player is not None:
        current_player.stop()

    video_player = TkinterVideo(root, scaled=True)
    video_player.load(r"{}".format(video_path))
    video_player.pack(expand=True, fill="both")
    video_player.play()

    # Update the current player
    current_player = video_player


# Create a GUI window
root = tk.Tk()
root.geometry("600x600")
root.title("Video Player")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

btn1 = tk.Button(button_frame, text="Ideal", command=lambda: play_video(video1))
btn1.pack(side=tk.LEFT, padx=10)

btn2 = tk.Button(button_frame, text="Speak", command=lambda: play_video(video2))
btn2.pack(side=tk.LEFT, padx=10)

btn3 = tk.Button(button_frame, text="Listen", command=lambda: play_video(video3))
btn3.pack(side=tk.LEFT, padx=10)

root.mainloop()
