# Hướng dẫn cài đặt sentiment analysis app và sentence similarity app


- Trước hết bạn nên sử dụng python 3.7 những bản mới hơn nhiều thư viện chưa hỗ trợ (link download mình để bên dưới)

## Cài đặt
```
git clone https://github.com/tuchau1404/nlp
cd nlp
pip install -r requirements.txt
```
## Chỉnh đường dẫn
- chỉnh lại đường dẫn của file jobs.csv tùy theo mỗi máy
```
df = pd.read_csv('jobs.csv')
```
## Chạy app
```
streamlit run sentiment.py
streamlit run similarity.py
```

- [link](https://python.en.uptodown.com/windows/download/2114753) download python mình đang sử dụng
- [link](https://youtu.be/63D20EBuUXc) video demo sentiment analysis
- [link](https://youtu.be/5aYvkftOA6s) video demo sentence similarity
  
     
