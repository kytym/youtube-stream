import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title("プログレスバーの表示")
"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Done!"

st.title("Streamlit 入門")

st.write("Image")

if st.checkbox("Show Image"):
    img = Image.open("mlynar.png")
    st.image(img, caption="Mlynar", use_column_width=100)

option = st.selectbox(
    "数字を入力してください",
    list(range(1,11))
)

"入力した数字は",option,"です"

st.write("Interactice Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

text = st.text_input("趣味を教えてください")
condition= st.slider("今の調子は？", 0, 100, 50)

"あなたの趣味は",text,"です。"
"コンディション:", condition

df = pd.DataFrame(    
    np.random.rand(20,3),
    columns=["a","b","c"]
)





#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)