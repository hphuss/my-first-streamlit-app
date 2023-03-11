import streamlit as st
c=st.write("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')

if st.button('Giải'):
  if a != 0:
    st.write("Phương trình có 1 nghiệm", (-b)/a)
  else:
    st.write("Phương trình vô nghiệm")
