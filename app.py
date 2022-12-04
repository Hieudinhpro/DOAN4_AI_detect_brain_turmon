import streamlit as st
from PIL import Image
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img

st.markdown("<h2>Detect brain tumor using neural networks</h2>",unsafe_allow_html=True)
st.sidebar.markdown("<h2>Tran Dinh Hieu</h2>",unsafe_allow_html=True)
st.sidebar.markdown("<h3>20IT212</h3>",unsafe_allow_html=True)
st.sidebar.markdown("---")
opt =st.sidebar.radio("Select the model", options=['cnn','vgg16', 'resnet50','inceptionV3'])

#define model
Inceptionv3=tf.keras.models.load_model("/home/hieudinhos/DOAN4/InceptionV3.h5")
CNN=tf.keras.models.load_model("/home/hieudinhos/DOAN4/CNN_tumor.h5")
VGG16=tf.keras.models.load_model("/home/hieudinhos/DOAN4/CNN_tumor.h5")
Resnet50=tf.keras.models.load_model("/home/hieudinhos/DOAN4/CNN_tumor.h5")


if opt=="vgg16":
    st.header("VGG16 Model")
    st.markdown("---")
    image_VGG16=st.file_uploader("Uploads file at here", type=['png','jpg','jpeg'])
    col1, col2 = st.columns(2)
    info=col2.empty()
    size=col2.empty()
    mode=col2.empty()
    format=col2.empty()
    if image_VGG16 is not None :
        col1.image(image_VGG16,width=350)
        images=Image.open(image_VGG16)
        info.markdown(f"<h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Information of image </h5>",unsafe_allow_html=True)
        size.text(f"size {images.size}  " )
        mode.text(f"mode {images.mode}  " )
        format.text(f"format {images.format}  " )
        img = load_img(image_VGG16, target_size=(224, 224))  # this is a PIL image
        x = img_to_array(img)  # Numpy array with shape (150, 150, 3)
        x = x.reshape((1,) + x.shape)
        x /= 255
        resu=VGG16.predict(x)
        st.text(f"In this case, the probability of having a tumor is as : {resu[0][0]} %")
    else :
        pass
    st.markdown('---')
    st.markdown("<h5>h</h5>",unsafe_allow_html=True)

elif opt=="cnn":
    st.header("CNN Model")
    st.markdown("---")
    image_CNN=st.file_uploader("Uploads file at here", type=['png','jpg','jpeg'])
    col1, col2 = st.columns(2)
    info=col2.empty()
    size=col2.empty()
    mode=col2.empty()
    format=col2.empty()
    if image_CNN is not None :
        col1.image(image_CNN,width=350)
        images=Image.open(image_CNN)
        info.markdown(f"<h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Information of image </h5>",unsafe_allow_html=True)
        size.text(f"size {images.size}  " )
        mode.text(f"mode {images.mode}  " )
        format.text(f"format {images.format}  " )
        img = load_img(image_CNN, target_size=(224, 224))  # this is a PIL image
        x = img_to_array(img)  # Numpy array with shape (150, 150, 3)
        x = x.reshape((1,) + x.shape)
        x /= 255
        resu=CNN.predict(x)
        st.text(f"In this case, the probability of having a tumor is as : {resu[0][0]} %")
    else :
        pass
    st.markdown('---')
    st.markdown("<h5>h</h5>",unsafe_allow_html=True)

elif  opt=="inceptionV3" :
    st.header("InceptionV3 Model")
    st.markdown("---")
    image_Inceptionv3=st.file_uploader("Uploads file at here", type=['png','jpg','jpeg'])
    col1, col2 = st.columns(2)
    info=col2.empty()
    size=col2.empty()
    mode=col2.empty()
    format=col2.empty()
    if image_Inceptionv3 is not None :
        col1.image(image_Inceptionv3,width=350)
        images=Image.open(image_Inceptionv3)
        info.markdown(f"<h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Information of image </h5>",unsafe_allow_html=True)
        size.text(f"size {images.size}  " )
        mode.text(f"mode {images.mode}  " )
        format.text(f"format {images.format}  " )
        img = load_img(image_Inceptionv3, target_size=(224, 224))  # this is a PIL image
        x = img_to_array(img)  # Numpy array with shape (150, 150, 3)
        x = x.reshape((1,) + x.shape)
        x /= 255
        resu=Inceptionv3.predict(x)
        st.text(f"In this case, the probability of having a tumor is as : {resu[0][0]} %")
    else :
        pass
    st.markdown('---')
    st.markdown("<h5>h</h5>",unsafe_allow_html=True)

else :
    st.header("Resnet50 Model")
    st.markdown("---")
    image_Resnet50=st.file_uploader("Uploads file at here", type=['png','jpg','jpeg'])
    col1, col2 = st.columns(2)
    info=col2.empty()
    size=col2.empty()
    mode=col2.empty()
    format=col2.empty()
    if image_Resnet50 is not None :
        col1.image(image_Resnet50,width=350)
        images=Image.open(image_Resnet50)
        info.markdown(f"<h5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Information of image </h5>",unsafe_allow_html=True)
        size.text(f"size {images.size}  " )
        mode.text(f"mode {images.mode}  " )
        format.text(f"format {images.format}  " )
        img = load_img(image_Resnet50, target_size=(224, 224))  # this is a PIL image
        x = img_to_array(img)  # Numpy array with shape (150, 150, 3)
        x = x.reshape((1,) + x.shape)
        x /= 255
        resu=Resnet50.predict(x)
        st.text(f"In this case, the probability of having a tumor is as : {resu[0][0]} %")
    else :
        pass
    st.markdown('---')
    st.markdown("<h5>h</h5>",unsafe_allow_html=True)

st.sidebar.markdown("---")


 