import streamlit as st
import pandas as pd 

st.set_page_config('Amazon Recommendation System') # To Run the file (streamlit run app.py)

org_list = pd.read_csv('Saree_removed_duplicate.csv')
similarity = pd.read_csv('recomended_saree.csv')

def recommend(index): # Orignal duplicate removed dataset
    df = org_list.iloc[similarity.iloc[index].tolist()[1:]]
    return df


st.title('Amazon Srees Recommndation System')
option = st.selectbox(  
    "Type or select a saree number from the dropdown",
    org_list['index'].values)

st.image(org_list['imag_url'].values[option])
st.markdown('<p style="text-align: center; font-weight: bold;">{}</p>'.format(org_list['brand'].values[option]), unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">{}</p>'.format(org_list['name'].values[option]), unsafe_allow_html=True)
st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(org_list['disc_price'].values[option], org_list['act_price'].values[option]), unsafe_allow_html=True)


if st.button('Recommended'):
    recomndation = recommend(option)
    
    count = 0

    for i in range(4):
        for j in st.columns(3):
            if count == 10:
                break
            with j :
                st.image(recomndation['imag_url'].values[count])
                st.markdown('<p style="text-align: center; font-weight: bold;">{}</p>'.format(recomndation['brand'].values[count]), unsafe_allow_html=True)
                st.markdown('<p style="text-align: center;">{}</p>'.format(recomndation['name'].values[count]), unsafe_allow_html=True)
                st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(recomndation['disc_price'].values[count], recomndation['act_price'].values[count]), unsafe_allow_html=True)

            count +=1