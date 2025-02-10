# py02_turtle.py
# 터틀 라이브러리는 주피터노트북에서 실행 불가
import turtle as t

t.home()
t.shape('turtle')

for i in range(10):
    t.forward(100)
    t.left(108)
t.done() # 반드시 필요