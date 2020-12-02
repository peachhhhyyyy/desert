import turtle as t
import random
score = 0
t.title("사막에서 우물 찾기")

# bg 보여주기
def showBg():
    bp = t.Screen()
    bp.setup(600,600)
    bp.bgpic("desert.gif")

# 사방으로 setheading 정하기
def r(): t.setheading(0)
def u(): t.setheading(90)
def l(): t.setheading(180)
def d(): t.setheading(270)
def s(): 
    t.clear()
    t.forward(10)
    te.forward(7)
    te.goto(0, 200)
    tf.goto(0, -200)
    t.goto(0,0)
    t.showturtle()
    te.showturtle()
    tf.showturtle()
    play()

# 플레이 함수
def play():
    global score
    global text
    t.forward(10)
    te.forward(8)
    angle = te.towards(t.pos())
    te.setheading(angle)
    if t.distance(tf) < 20: # 우물이 랜덤으로 바뀔 때
        tfx = random.randint(-150, 150)
        tfy = random.randint(-150, 150)
        score = score + 1
        t.write(score, move=False, align='center', font=("Arial",10,"bold"))
        tf.goto(tfx, tfy)
    if t.distance(te) < 10: # 잡힐 때
        text = '점수: '+ str(score)+'점'
        x = (t.window_width() / 2) - 300
        y = (t.window_height() / 2) - 300
        t.setpos(x, y)
        t.write(text, move=False, align='center', font=("Arial",20,"bold"))
        score = 0
        gameOverText()
        quitGame()
    else:
        t.ontimer(play, 100)

# 게임이 끝났다는 텍스트 보여주기
def gameOverText():
    x = (t.window_width() / 2) - 300
    y = (t.window_height() / 2) - 150
    t.setpos(x, y)
    t.write("Game Over", move=False, align='center', font=("Arial",30,"bold","underline"))
    t.hideturtle()
    te.hideturtle()
    tf.hideturtle()
    tf.clear()
    te.clear()

# 게임 다시시작
def quitGame():
    x = (t.window_width() / 2) - 300
    y = (t.window_height() / 2) - 400
    t.setpos(x, y)
    t.write("게임을 다시 시작하려면 스페이스바를 누르세요!", move=False, align='center', font=("Malgun Gothic",14,"normal"))
    t.hideturtle()
    te.hideturtle()
    tf.hideturtle()
    tf.clear()

# 적 선언
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 우물 선언
tf = t.Turtle()
tf.shape("circle")
tf.shapesize(3)
tf.color("#1a73e8")
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 주인공 선언
t.shape("turtle")
t.color("white")
t.speed(0)
t.up()
t.onkeypress(r, "Right")
t.onkeypress(u, "Up")
t.onkeypress(l, "Left")
t.onkeypress(d, "Down")
t.onkeypress(s, "space")
t.listen()

showBg()
play()

t.mainloop()