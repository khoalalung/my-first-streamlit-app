import streamlit as st
import sklearn
import plotly
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st. button('Giải'):
	st.write('Phương trình có 1 nghiệm là', -b/a)
