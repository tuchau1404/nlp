from transformers import pipeline
import streamlit as st


@st.cache()
def pred(user_input):
    candidate_labels = ["positive", "negative", "not sure"]
    classifier = pipeline("zero-shot-classification")
    content = classifier(user_input, candidate_labels)
    return content


if __name__ == '__main__':

    
    text = 'Today is a good day'
    
    st.title('SENTIMENT ANALYSIS')
    user_input = st.text_input("Enter your feelings", text)
    if user_input !="":
        content = pred(user_input)
        if content['labels'][0] == 'positive':
            st.write('**Positive**', '\U0001F60A','\U0001F60A')
        elif content['labels'][0] == 'negative':
            st.write('**Negative**', '\U0001F641','\U0001F641')
        else:
            st.write('**Not sure**')



