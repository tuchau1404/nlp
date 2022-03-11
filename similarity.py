from sentence_transformers import SentenceTransformer,util
from pyvi.ViTokenizer import tokenize
import streamlit as st 
import pandas as pd
import random 
flag = False

@st.cache(allow_output_mutation=True)
def load_es():
    model_embedding = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')    
    df = pd.read_csv('s3-nlp3\jobs.csv')
    return model_embedding,df

def similarity_percent(embeddings_1, embeddings_2):
    return float("{:.4f}".format(util.pytorch_cos_sim(embeddings_1, embeddings_2)[0][0]))

def run():
    st.title('SENTENCE SIMILARITY')
    page = st.radio('Mode',['Random','Input'])
    if page =='Random':
        with st.form("my_form"):
            number_1= random.randrange(0,len(df), 1)
            number_2 = random.randrange(0,len(df), 1)
            number_3= random.randrange(0,len(df), 1)
            word_1 = st.text_input('sentence 1',df['Jobs'][number_1])
            word_2 = st.text_input('sentence 2',df['Jobs'][number_2])
            word_3 = st.text_input('sentence 3',df['Jobs'][number_3])
            
            sentences= [word_1,word_2,word_3]
            sentences_tokenizer = [tokenize(sentence) for sentence in sentences]
            embeddings = model_embedding.encode(sentences_tokenizer)
            result0_1 =similarity_percent(embeddings[0],embeddings[1])
            result1_2 = similarity_percent(embeddings[1],embeddings[2])
            result2_0 = similarity_percent(embeddings[2],embeddings[0])
            if st.form_submit_button('Random'):
                pass
        
    else:
        with st.form("my_form"):
            word_1 = st.text_input('sentence 1')
            word_2 = st.text_input('sentence 2')
            word_3 = st.text_input('sentence 3')
            sentences= [word_1,word_2,word_3]
            sentences_tokenizer = [tokenize(sentence) for sentence in sentences]
            embeddings = model_embedding.encode(sentences_tokenizer)
            result0_1 =similarity_percent(embeddings[0],embeddings[1])
            result1_2 = similarity_percent(embeddings[1],embeddings[2])
            result2_0 = similarity_percent(embeddings[2],embeddings[0])
            if st.form_submit_button('Calculate'):
                pass

    st.write('**Similarity between sentence 1 and sentence 2 is** ',result0_1)
    st.write('**Similarity between sentence 2 and sentence 3 is** ',result1_2)
    st.write('**Similarity between sentence 1 and sentence 3 is** ',result2_0)
  

if __name__ == '__main__':
    model_embedding,df = load_es()
    run()
    
