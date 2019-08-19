import sda
import scipy.io.wavfile as wav
from PIL import Image
import numpy as np
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import *

if __name__ == '__main__':
    message = "Thank you for your donation through Streamers Tips"
    language = 'en'
    tts = gTTS(text=message, lang=language, slow=False)
    tts.save('example/message_audio.mp3')
    sound = AudioSegment.from_mp3('example/message_audio.mp3')
    sound.export("example/message_audio.wav", format="wav")
    va = sda.VideoAnimator(gpu=-1)  # Instantiate the animator
    fs, audio_clip = wav.read("example/message_audio.wav")
    frame = np.array(Image.open("example/face_gil.bmp"))
    #frame = "example/image.bmp"
    vid, aud = va(frame, audio_clip, fs=fs)
    #vid, aud = va("example/image.bmp", audio_clip, fs=fs)
    va.save_video_raw(vid)
    
    #imageio.mimwrite("extracted.mp4", vid, fps=fs)
    #aclip = AudioFileClip('example/message_audio.wav')
    #clip = VideoFileClip('extracted_st.mp4')
    #clip.set_audio(aclip)
    #clip.write_videofile('final_vid.mp4')