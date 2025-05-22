import streamlit as st

studentimage = st.file_uploader('Upload student image here',['jpg','jpeg','png'])

if studentimage:
    st.image(studentimage)

    if st.button("Save Student Image"):
        picname = 'studentimage'
        with open(f'{picname}.png','wb') as writepic:
            writepic.write(studentimage.getbuffer())
        st.success("Image Saved")