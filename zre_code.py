import streamlit as st
from PIL import Image
import pandas as pd

opt =st.sidebar.radio("select the model ", options=['vgg16','cnn', 'resnet'])
if opt=="vgg16":
    st.text("vgg16")
    image=st.file_uploader("please uploads file", type=['png','jpg','jpeg'])
    size=st.empty()
    mode=st.empty()
    format=st.empty()

    if image is not None :
        st.image(image,width=600)
        image=Image.open(image)
        size.markdown(f"<h6>size {image.size} </h6>",unsafe_allow_html=True)
        mode.markdown(f"<h6>mode {image.mode} </h6>",unsafe_allow_html=True)
        format.markdown(f"<h6>format {image.format} </h6>",unsafe_allow_html=True)
    else :
        pass
elif opt=="cnn":
    st.text("cnn")
else :
    st.text("resnet")
st.markdown('---')


val=st.slider("value slide", min_value=0, max_value=10)
st.text(val)

text_input=st.text_input("enter into me")
st.text(text_input)
text_input_area=st.text_area("enter into me")
st.text(text_input_area)

# bar = st.progress(0)
# import time
# for i in range(10):
#     bar.progress((i+1)*10)
#     time.sleep(1)

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
       st.warning("noo")
       st.success("ok")
table=pd.DataFrame({"id":[1 ,2 ,3 ,4 ,5],
                   "id2":[1 ,2 ,3 ,4 ,5],
                   "id3":[1 ,2 ,3 ,4 ,5] })
st.table(table )
st.dataframe(table)

 