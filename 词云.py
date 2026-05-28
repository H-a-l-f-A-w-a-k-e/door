import wordcloud as wc
import jieba as j

with open(r'C:\Users\34177\Desktop\123.txt',encoding='utf-8') as f:
    ls=j.lcut(f.read())
w=wc.WordCloud(
    width=1000,height=700,
    background_color='white',
    font_path='C:\Windows\Fonts/msyh.ttc'
    )
txt=' '.join(ls)
w.generate(txt)
w.to_file('123.png')