import streamlit as st
import unimodular_chaos_encryption as uce
from PIL import Image
import numpy as np

# def encrypt(img, pass_1, pass_2):
#     uce.encrypt(img, pass_1, pass_2)

# def decrypt(img, pass_1, pass_2):
#     uce.decrypt(img, pass_1, pass_2)

# def encrypted_img(img):
#     col1.write("Original Image :camera:")
#     col1.image(image)

    # encrypted_img = encrypt(img, pass_1, pass_2)
    # col2.write("Encrypted Image :closed_lock_with_key:")
    # st.sidebar.markdown("\n")
    # st.sidebar.download_button("Download encrypted image", encrypted_img, "encrypted.png", "image/png")

def main():
    st.set_page_config(layout="wide", page_title="")

    st.write("## Image Encryptor")
    st.write(
        ## Add stuff here about the webapp lols
    )

    st.sidebar.write("## Upload and download :gear:")
    col1, col2 = st.columns(2)

    if 'image' not in st.session_state:
        st.session_state['image'] = None

    image_path = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
     
    if st.write(st.session_state['image']) is None:
        image = Image.open("nature.png")
    if image_path is not None:
        st.session_state['image'] = image_path  
        image = Image.open(image_path)
 
    pass_1_choices = uce.factors(np.array(image).size) # Array of keys for pass 1 - need to reset per upload

    pass_1 = int(st.selectbox('Choose a key:', pass_1_choices))
    pass_2 = st.text_input("Enter your password", value=0)
    pass_2 = float("0." + pass_2 + "1")

    print(pass_1, "type: ", type(pass_1))
    print(pass_2, "type: ", type(pass_2))

    encrypted = uce.encrypt("nature.png", pass_1, pass_2)
    col1.image(image)
    col2.image(encrypted)

    # if image_path is not None:
    #     encrypted_img(image)
    # else:
    #     encrypted_img("nature.png") # default 

if __name__ == "__main__":
    main()