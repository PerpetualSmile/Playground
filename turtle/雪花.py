from turtle import *


def Koch(length):
    if length < 20:
        fd(length)
        return
    Koch(length/3)
    lt(60)
    Koch(length/3)
    rt(120)
    Koch(length/3)
    lt(60)
    Koch(length/3)

def snowflake(n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        Koch(n)
        rt(120)

if __name__ == '__main__':
    speed(10)
    snowflake(100)