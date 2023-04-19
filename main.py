import streamlit as st
import unimodular_chaos_encryption as uce
from PIL import Image

# def encrypt(img, pass_1, pass_2):
#     uce.encrypt(img, pass_1, pass_2)

# def decrypt(img, pass_1, pass_2):
#     uce.decrypt(img, pass_1, pass_2)

def encrypted_img(img):
    image = Image.open(img)
    col1.write("Original Image :camera:")
    col1.image(image)

    # encrypted_img = encrypt(img, pass_1, pass_2)
    # col2.write("Encrypted Image :closed_lock_with_key:")
    # st.sidebar.markdown("\n")
    # st.sidebar.download_button("Download encrypted image", encrypted_img, "encrypted.png", "image/png")


pass_1 = [1,2,3,4,5,6]

st.set_page_config(layout="wide", page_title="")

st.write("## Image Encryptor")
st.write(
     ## Add stuff here about the webapp lols
)
st.sidebar.write("## Upload and download :gear:")

st.selectbox('Choose a key:', pass_1)
pass_2 = st.text_input("Enter your password")

col1, col2 = st.columns(2)
image = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if image is not None:
    encrypted_img(image)
else:
    encrypted_img("nature.png") # default 