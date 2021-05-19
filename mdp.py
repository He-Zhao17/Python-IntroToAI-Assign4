
### code for representing/solving an MDP
### Most of this is complete. You should only need to complete the valueIteration and policyIteration methods.

import random

class State :

    def __init__(self, coordString=None) :
        self.utility = 0
        self.reward = 0.0
        ### an action maps to a list of probability/state pairs
        self.transitions = {}
        self.actions = []
        self.policy = None
        self.coords = coordString
        self.isGoal = False

    def computeEU(self, action) :
        return sum([trans[0] * trans[1].utility 
                    for trans in self.transitions[action]])

    def selectBestAction(self) :
        best = max([(self.computeEU(a), a) for a in self.actions])
        return best[1]

    def __eq__(self, other) :
        return self.coords == other.coords

    def __hash__(self) :
        return self.coords.__hash__()


class Map :

    def __init__(self) :
        self.states = {}
        self.error = 0.01
        self.gamma = 0.8

    def getState(self, name) :
        try :
            return self.states[name]
        except KeyError :
            return None

### you do this one.
    def valueIteration(self) :
        

### you do this one.        
    def policyIteration(self) :



    def getMapFromFile(self, fname) :
        with open(fname) as infile :
            for line in infile :
                if line.startswith("#") or len(line) < 2 :
                    pass
                elif line.startswith("gamma") :
                    self.gamma = float(line.split(":")[1])
                elif line.startswith("error") :
                    self.error = float(line.split(":")[1])
                elif line.startswith("reward") :
                    reward = float(line.split(":")[1])
                elif line.startswith("goals") :
                    gs = line.split(":")[1]
                    values = gs.split()
                    for i in range(0,len(values),2) :
                        self.states[values[i]] = State(values[i])
                        self.states[values[i]].isGoal = True
                        self.states[values[i]].utility = float(values[i+1])
                        self.states[values[i]].reward = float(values[i+1])
                ### state transitions
                else :
                    values = line.split()
                    if values[0] not in self.states :
                        self.states[values[0]] = State(values[0])
                        self.states[values[0]].isGoal = False
                        self.states[values[0]].reward = reward
                    action = values[1]
                    self.states[values[0]].actions.append(action)
                    transitions = []
                    for x in values[2:] :
                        prob, name = x.split(":") 
                        if not self.getState(name) :
                            self.states[name] = State(name)
                            self.states[name].isGoal = False
                            self.states[name].reward = reward
                        transitions.append((float(prob), self.getState(name)))
                    self.states[values[0]].transitions[action] = transitions
