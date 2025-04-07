import streamlit as st
import tempfile
from scenechange import detect_scene_changes

st.title("Video Scene Change Detection")

if "processed" not in st.session_state:
    st.session_state.processed=False


uploaded_file=st.file_uploader("Upload Video",type=["mp4","avi","mov"],accept_multiple_files=False)
if uploaded_file is not None:

    temp_video=tempfile.NamedTemporaryFile(delete=False,suffix=".mp4")
    temp_video.write(uploaded_file.read())
    temp_video_path = temp_video.name
    output_file="scene_changes.txt"

    
    if not st.session_state.processed:
        with st.spinner("Processing Video"):
            detect_scene_changes(temp_video_path,output_file=output_file,verbose=True)
            st.session_state.processed=True

    try:
        with open(output_file, "r") as f:
            file_content = f.read()
        st.subheader("📃 Scene Change Timestamps")
        st.code(file_content, language="text")

        with st.spinner("Downloading:"):
            with open(output_file, "r") as f:
                st.download_button(
                    label="Download File",
                    data=f,
                    file_name="scenechange.txt",
                    mime="text/plain" 
                )                              


    except FileNotFoundError:
        st.error("scene_change.txt was not found. Make sure it was created by detect_scene_changes().")