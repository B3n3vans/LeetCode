import random

def coinToss():
    rand_i = random.randint(0,1)
    outcomes = ["Heads","Tails"]
    return outcomes[rand_i]

t1 = coinToss()
t2 = coinToss()
t3 = coinToss()

print(t1,t2,t3)