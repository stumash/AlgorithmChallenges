import math

def main():
    logoqty = int(input())
    while(logoqty > 0):
        logoqty -= 1

        angle = 0
        pos = (0,0)

        moveqty = int(input())
        while (moveqty > 0):
            moveqty -= 1
            move = [token for token in input().split(' ')]
            movetype = move[0]
            movesize = int(move[1])

            if (movetype == "fd" or movetype == "bk"):
                posdx = math.cos(math.radians(angle)) * movesize
                posdy = math.sin(math.radians(angle)) * movesize
                if (movetype == "fd"):
                    pos = (pos[0] + posdx, pos[1] + posdy)
                else:
                    pos = (pos[0] - posdx, pos[1] - posdy)
            elif (movetype == "lt"):
                angle = (angle + movesize) % 360
            else:
                angle = (angle - movesize) % 360

        print(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2)))

if __name__ == "__main__":
    main()
