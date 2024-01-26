"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel, GRect
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.ball
    ball_width = graphics.ball.width
    paddle = graphics.paddle
    window = graphics.window
    brick_rows = graphics.get_brick_rows()
    brick_cols = graphics.get_brick_rows()

    brick_count = brick_rows*brick_cols

    lives = NUM_LIVES
    lives_label = GLabel("LIVES: " + str(lives))
    window.add(lives_label, x=window.width-50, y=window.height-5)

    score = 0
    score_label = GLabel("SCORE: " + str(score))
    window.add(score_label, x=0, y=window.height-5)

    graphics.set_ball_velocity()
    vx = graphics.get_dx()
    vy = graphics.get_dy()

    while True:  # while graphics.starting會失效, 因為graphics.starting只要一出現False, 迴圈就無法執行
        pause(FRAME_RATE)
        if brick_count == 0:
            window.remove(ball)
            win = GLabel("VICTORY")  # 遊戲勝利
            win.font = "ravie-30"
            win.color = "#009593"
            window.add(win, x=(window.width-win.width)/2, y=(window.height-win.height)/2+50)
            break
        elif lives == 0:  # 遊戲結束
            window.remove(ball)
            lose = GLabel("GAME OVER !")
            lose.font = "ravie-30"
            lose.color = "#a31d14"
            window.add(lose, x=(window.width-lose.width)/2, y=(window.height-lose.height)/2+50)
            break
        while graphics.starting:
            pause(FRAME_RATE)
            score_label.text = "SCORE: " + str(score)
            ball.move(vx, vy)
            if ball.y + ball_width > window.height:  # ball沒接到
                lives -= 1
                lives_label.text = "LIVES: " + str(lives)
                if lives > 0 or brick_count > 0:
                    window.add(ball, x=(window.width-ball_width)/2, y=(window.height-ball_width)/2)
                    graphics.starting = False
                    graphics.set_ball_velocity()  # 球掉了之後,重新給予初始速度
                    vx = graphics.get_dx()
                    vy = graphics.get_dy()
                break

            if ball.x < 0 or ball.x + ball.width > window.width:  # ball碰到牆
                vx = -vx
                ball.move(vx, vy)
                break
            elif ball.y < 0:
                vy = -vy
                ball.move(vx, vy)
                break

            # 判別有無撞到前再去抓座標，不然會抓到移動前的數據
            ball_tl = window.get_object_at(ball.x, ball.y)
            ball_tr = window.get_object_at(ball.x + ball_width, ball.y)
            ball_bl = window.get_object_at(ball.x, ball.y + ball_width)
            ball_br = window.get_object_at(ball.x + ball.width, ball.y + ball.width)
            if (ball_tl or ball_tr or ball_bl or ball_br) is not None:  # ball碰到板子或磚塊
                if (ball_tl or ball_tr or ball_bl or ball_br) is paddle:  # 碰到板子反彈
                    vy = -vy
                    ball.move(vx, vy)
                    break
                elif((ball_tl or ball_tr or ball_bl or ball_br) is lives_label) or \
                        ((ball_tl or ball_tr or ball_bl or ball_br) is score_label):  # 碰到記分板or記命版or特殊方塊
                    pass
                else:
                    if ball_tl is not None and (paddle or lives_label or score_label):
                        if window.remove(ball_tr):
                            score += 1
                            brick_count -= 1
                            vy = -vy
                    elif ball_tr is not None and (paddle or lives_label or score_label):
                        if window.remove(ball_tr):
                            score += 1
                            brick_count -= 1
                            vy = -vy
                    elif ball_bl is not None and (paddle or lives_label or score_label):
                        if window.remove(ball_bl):
                            score += 1
                            brick_count -= 1
                            vy = -vy
                    elif ball_br is not None and (paddle or lives_label or score_label):
                        if window.remove(ball_br):
                            score += 1
                            brick_count -= 1
                            vy = -vy
                    break

                # elif (ball_tl or ball_tr or ball_bl or ball_br) is not (paddle or lives_label or score_label):  # 碰到磚塊
                #     if window.remove(ball_tl):
                #         score += 1
                #         brick_count -= 1
                #     if window.remove(ball_tr):
                #         score += 1
                #         brick_count -= 1
                #     if window.remove(ball_bl):
                #         score += 1
                #         brick_count -= 1
                #     if window.remove(ball_br):
                #         score += 1
                #         brick_count -= 1
                #     score_label.text = "SCORE: " + str(score)
                #     vy = -vy


if __name__ == '__main__':
    main()
