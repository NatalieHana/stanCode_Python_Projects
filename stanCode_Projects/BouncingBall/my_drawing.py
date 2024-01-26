"""
File: my_drawing.py
Name: Jane
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: 2024

    Make wish to daruma for good luck 2024
    """
    window = GWindow(width=500, height=500, title="Daruma")

    bk_w = GRect(window.width, window.height)
    bk_w.filled = True
    bk_w.fill_color = "#F8E5AE"
    bk_w.color = "#F8E5AE"
    window.add(bk_w)

    body = GOval(250, 300, x=120, y=110)
    body.filled = True
    body.fill_color = "#C40E03"
    body.color = "#C40E03"
    window.add(body)

    down_body = GOval(275, 260, x=110, y=160)
    down_body.filled = True
    down_body.fill_color = "#C40E03"
    down_body.color = "#C40E03"
    window.add(down_body)

    face = GOval(180, 125, x=155, y=135)
    face.filled = True
    face.fill_color = "#FEDCD0"
    face.color = "#FEDCD0"
    window.add(face)

    down_face = GOval(190, 125, x=150, y=170)
    down_face.filled = True
    down_face.fill_color = "#FEDCD0"
    down_face.color = "#FEDCD0"
    window.add(down_face)

    l_eye_w = GOval(45, 45, x=190, y=180)
    l_eye_w.filled = True
    l_eye_w.fill_color = "white"
    l_eye_w.color = "white"
    window.add(l_eye_w)

    l_eye_b = GOval(30, 30, x=197, y=188)
    l_eye_b.filled = True
    l_eye_b.fill_color = "black"
    l_eye_b.color = "black"
    window.add(l_eye_b)

    r_eye_w = GOval(45, 45, x=265, y=180)
    r_eye_w.filled = True
    r_eye_w.fill_color = "white"
    r_eye_w.color = "white"
    window.add(r_eye_w)

    r_eye_b = GOval(30, 30, x=272, y=188)
    r_eye_b.filled = True
    r_eye_b.fill_color = "black"
    r_eye_b.color = "black"
    window.add(r_eye_b)

    l_eyebrow = GArc(150, 55, 265, -95)
    l_eyebrow.filled = True
    l_eyebrow.fill_color = "black"
    l_eyebrow.color = "black"
    window.add(l_eyebrow, x=190, y=145)

    r_eyebrow = GArc(150, 55, 275, 95)
    r_eyebrow.filled = True
    r_eyebrow.fill_color = "black"
    r_eyebrow.color = "black"
    window.add(r_eyebrow, x=230, y=145)

    shift = 0
    for i in range(3):
        shift += 1
        mouth = GArc(80, 60, 0, 180)
        mouth.color = "#E14128"
        window.add(mouth, x=210, y=240+shift)

    mouth_l = GOval(8, 8, x=207, y=249)
    mouth_l.filled = True
    mouth_l.fill_color = "#E14128"
    mouth_l.color = "#E14128"
    window.add(mouth_l)

    mouth_r = GOval(8, 8, x=287, y=249)
    mouth_r.filled = True
    mouth_r.fill_color = "#E14128"
    mouth_r.color = "#E14128"
    window.add(mouth_r)

    shift = 0
    for i in range(8):
        shift += 1
        beard_l = GLine(230, 260, 210+shift, 280)
        window.add(beard_l)

    shift = 0
    for i in range(8):
        shift += 1
        beard_c = GLine(250, 260, 246+shift, 285)
        window.add(beard_c)

    shift = 0
    for i in range(10):
        shift += 1
        beard_r = GLine(270, 260, 286+shift, 280)
        window.add(beard_r)

    l_bb = GArc(45, 65, 80, 230)
    l_bb.filled = True
    l_bb.fill_color = "black"
    window.add(l_bb, x=160, y=200)

    l_1 = GRect(10, 4, x=175, y=220)
    l_1.filled = True
    l_1.fill_color = "#FEDCD0"
    l_1.color = "#FEDCD0"
    window.add(l_1)

    l_2 = GRect(12, 4, x=170, y=233)
    l_2.filled = True
    l_2.fill_color = "#FEDCD0"
    l_2.color = "#FEDCD0"
    window.add(l_2)

    l_3 = GRect(15, 4, x=175, y=245)
    l_3.filled = True
    l_3.fill_color = "#FEDCD0"
    l_3.color = "#FEDCD0"
    window.add(l_3)

    r_bb = GArc(35, 65, 100, -230)
    r_bb.filled = True
    r_bb.fill_color = "black"
    window.add(r_bb, x=305, y=200)

    r_1 = GRect(10, 4, x=315, y=220)
    r_1.filled = True
    r_1.fill_color = "#FEDCD0"
    r_1.color = "#FEDCD0"
    window.add(r_1)

    r_2 = GRect(12, 4, x=315, y=233)
    r_2.filled = True
    r_2.fill_color = "#FEDCD0"
    r_2.color = "#FEDCD0"
    window.add(r_2)

    r_3 = GRect(15, 4, x=310, y=245)
    r_3.filled = True
    r_3.fill_color = "#FEDCD0"
    r_3.color = "#FEDCD0"
    window.add(r_3)

    luck = GLabel("福", x=205, y=395)
    luck.font = "標楷體-65"
    luck.color = "#B48E40"
    window.add(luck)

    body_l1 = GArc(50, 80, 90, 180)
    body_l1.filled = True
    body_l1.fill_color = "#B48E40"
    body_l1.color = "#B48E40"
    window.add(body_l1, x=190, y=310)

    body_l2 = GArc(50, 80, 80, 180)
    body_l2.filled = True
    body_l2.fill_color = "#B48E40"
    body_l2.color = "#B48E40"
    window.add(body_l2, x=155, y=290)

    body_l3 = GArc(50, 60, 80, 180)
    body_l3.filled = True
    body_l3.fill_color = "#B48E40"
    body_l3.color = "#B48E40"
    window.add(body_l3, x=125, y=280)

    body_r1 = GArc(50, 80, 90, -180)
    body_r1.filled = True
    body_r1.fill_color = "#B48E40"
    body_r1.color = "#B48E40"
    window.add(body_r1, x=285, y=310)

    body_r2 = GArc(50, 80, 100, -180)
    body_r2.filled = True
    body_r2.fill_color = "#B48E40"
    body_r2.color = "#B48E40"
    window.add(body_r2, x=320, y=290)

    body_r3 = GArc(50, 60, 100, -180)
    body_r3.filled = True
    body_r3.fill_color = "#B48E40"
    body_r3.color = "#B48E40"
    window.add(body_r3, x=350, y=275)

    bk = GRect(100, 100, x=25, y=15)
    bk.filled = True
    bk.fill_color = "red"
    bk.color = "red"
    window.add(bk)

    label = GLabel(" 辰\n2024", x=40, y=110)
    label.font = "STXingkai-30"
    label.color = "white"
    window.add(label)


if __name__ == '__main__':
    main()
