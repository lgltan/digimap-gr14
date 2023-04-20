import streamlit as st
import unimodular_chaos_encryption as uce
import  streamlit_toggle as tog # pip install streamlit-toggle-switch
from PIL import Image
from io import BytesIO
import numpy as np

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def run(col1,col2,image_path, option):
    image = Image.open(image_path)
    image_array = np.array(image)
    col1.write("Original Image :camera:")
    col1.image(image)

    pass_1_choices = uce.factors(image_array.size) # Array of keys for pass 1 - need to reset per upload
    print(pass_1_choices)
    print("\n\n")
    pass_1 = int(st.selectbox('Choose a key:', pass_1_choices))
    pass_2 = st.text_input("Enter your password")
    

    if(pass_1 != "" and pass_2 != ""):
        pass_2 = float("0." + pass_2 + "1")                                                                                                         
        print(pass_1, "type: ", type(pass_1))
        print(pass_2, "type: ", type(pass_2))

        encrypted = uce.encrypt(image_path, pass_1, pass_2)
        image_array = np.array(encrypted)
        pass_2_choices = uce.factors(image_array.size)
        print(pass_2_choices)
        print("\n\n")

        if option: # Encrypt
            col2.write("Encrypted Image :closed_lock_with_key:")
            col2.image(encrypted)
            downloadable = convert_image(encrypted)
            st.sidebar.markdown("\n")
            st.sidebar.download_button("Download encrypted image", downloadable, "encrypted.png", "image/png")
        else:
            decrypted = uce.decrypt(encrypted, pass_1, pass_2)
            col2.write("Decrypted Image :unlock:")
            col2.image(decrypted)
            downloadable = convert_image(decrypted)
            st.sidebar.markdown("\n")
            st.sidebar.download_button("Download decrypted image", downloadable, "decrypted.png", "image/png")

def main():
    st.set_page_config(layout="wide", page_title="")
    st.write("## Image Encryptor")
    st.write(
        ## Add stuff here about the webapp lols
    )
    st.sidebar.write("## Upload and download :gear:")
    col1, col2 = st.columns(2)
    image_path = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    option = tog.st_toggle_switch(label="Encrypt", default_value=True, label_after=False)
    print(option)
    if image_path is not None:

        run(col1 ,col2, image_path, option)

if __name__ == "__main__":
    main()