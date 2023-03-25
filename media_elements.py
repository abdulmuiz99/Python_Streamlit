import streamlit as st

st.header("Display an image")
st.image('./media/image.jpg', caption='Beautiful Park', width=750)

st.header("Display Video")
video_files = open('./media/waterfalls.mp4', 'rb')
video_bytes = video_files.read()
st.video(video_bytes)

st.header("Display Audio")
audio_files = open('./media/audio.mp3', 'rb')
audio_bytes = audio_files.read()
st.audio(audio_bytes, format='audio/ogg')