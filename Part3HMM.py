from random import random

from pomegranate import *

summerDisc = DiscreteDistribution({'sunny' : 0.90, 'rainy' : 0.10})
winterDisc = DiscreteDistribution({'sunny' : 0.50, 'rainy' : 0.50})

summerSta = State(summerDisc, name = 'summer')
winterSta = State(winterDisc, name = 'winter')

model = HiddenMarkovModel()
model.add_states(summerSta, winterSta)

model.add_transition(model.start, summerSta, 0.50)
model.add_transition(model.start, winterSta, 0.50)
model.add_transition(summerSta, summerSta, 0.90)
model.add_transition(summerSta, winterSta, 0.10)
model.add_transition(winterSta, winterSta, 0.90)
model.add_transition(winterSta, summerSta, 0.10)
model.bake()

test = ['sunny', 'rainy', 'sunny', 'sunny']
testpre = model.predict(test)
print(test, '\n', testpre)


# make test samples

obsArr = [10, 20, 50 ,100]
for obs in obsArr:
    print('\n', obs)
    score = 0.0
    for i in range(1000):
        listObs, listStas = model.sample(length = obs, path = True)
        testpre = model.predict(listObs)
        tnum = 0
        for j in range(obs):
            if (testpre[j] == 0 and listStas[j + 1].name == 'summer') or (testpre[j] == 1 and listStas[j + 1].name == 'winter'):
                tnum += 1
        score += tnum / obs
    score = score / 1000
    print(score)


