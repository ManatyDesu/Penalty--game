import random
from time import sleep

Players = {"Player A":10, "Player B":10} #(key, value) = (name、HP)
Playerslist = list(Players.keys())
Player_num = len(Players.keys())
Attacklist = [1, 3, 5, 7]
Attack_num = len(Attacklist)
Kowai = ["Lion", "Badger", "Eagle", "Snake"]
Kowai_num = len(Kowai)
for i in range(Player_num):
        print(f"{Playerslist[i]}  HP  {Players[Playerslist[i]]}")
        sleep(2)
round = 1
while True:
    print(f"                        Round {round}!!!!                        ")
    print(f"-------------------------------------------------------------")
    sleep(2)
    Player = Playerslist[random.randint(0, Player_num-1)]
    Attack = Attacklist[random.randint(0, Attack_num-1)]
    print(Player+"は、", end="")
    print(Kowai[random.randint(0, 3)] + "によって", end="")
    print(str(Attack) + "ダメージ与えられた。")
    sleep(3)
    Players[Player] -= Attack
    print("残りHP")
    for i in range(Player_num):
        print(f"{Playerslist[i]}  HP  {Players[Playerslist[i]]}")
        sleep(2)
    if Players[Player] <= 0:
        break
    sleep(2)
    round += 1
print(f"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
print(f"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
print(f"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
print(f"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
print(f"{Player} is gameover!!")
