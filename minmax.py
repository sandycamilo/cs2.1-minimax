from sys import maxsize #pick maxsize of an integer - using value to represent infinity 

# +1 = human 
# -1 = computer 
#generate tree of all possible moves 
#each position or node of a tree holds a heuristic value - + / - 
#algorithm starts from bottom of tree, decides best move and removes all the bad moves 


#goal= pick up last stick

class Node(object): #node class makes each element for tree
  def __init__(self, i_depth, i_playerNum, i_Remainder, i_value = 0):
    self.i_depth = i_depth # how deep we are in tree - every iteration decreases value until we reach 0
    self.i_playerNum = i_playerNum # + or - human or computer
    self.i_Remainder = i_Remainder #sticks remaining 
    self.i_value = i_value #value that each node holds - -infinity or +infinity 
    self.children = [] #empty list children 
    self.CreateChildren() #creates the children

  def CreateChildren(self): 
    if self.i_depth >= 0: #check if we have passed the depth of 0 
      for i in range(1, 3): #how many sticks are we going to be removing
        v = self.i_Remainder - i #v holds value of how many sticks remain
        self.children.append( Node(self.i_depth -1, -self.i_playerNum, v, self.RealVal(v))) #when new child is created, depth is decreased by one, and the player is flipped (multiplied by -1), sticks remaning are passed (v),
                                                                                            #RealVal function is called and pass remaining sticks ~ 

  def RealVal(self, value): #determines if player has won or if the payer has taken a hold of more sticks and lost  
    if (value == 0): 
      return maxsize * self.i_playerNum
    elif (value < 0):
      return maxsize * -self.i_playerNum
    return 0 


def minmax(node, i_depth, i_playerNum): 
  if (i_depth == 0) or (abs(node.i_value) == maxsize): #if we are a depth of 0 or if we have reached a node is a win or lose condition ~ if they equal to maxsize (infinity)
    return node.i_value #if cases are true we return the value of node 

    i_bestValue = maxsize * -i_playerNum #assign value of infinity times the opposite direction of the player ~ if its neg they go + and viceversa

    for i in range(len(node.children)): #iterate through all of the children one by one for all possible choices
      child = node.children[i]
      i_val = minmax(child, i_depth -1, -i_playerNum) #run algorithm on all possible choices ~ drills to bottom of tree reducing the depth as it goes~ one by one and flipping the players
      if(abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)): #check distance of where we want to be from where we are currently are with current child, if value is closer to + or - infinity
        i_bestValue = i_val #store that best value

    return i_bestValue #return value

def WinCheck(i_sticks, i_playerNum): #checks if player/computer has made a selection that has won them a game or lost 
  if i_sticks <= 0:
    print("*" *30)
    if i_playerNum > 0:
      if i_sticks ==0:
        print("Win")
      else:
        print("Boo hoo")
    else:
      if i_sticks == 0:
        print("Better luch next time!")
      else: 
        print("Error")
    print("*"*30)
    return 0 
  return 1

if __name__ == '__main__':
  i_sticksTotal = 11 #starting with 11 sticks 
  i_depth = 4  # depth 
  i_curPlayer = 1 #starting with human player
  while (i_sticksTotal > 0): #start loops - as long as there are sticks keep iterating through function
    print("how many would you like to pick?")
    i_choice = input("1 or 2:") 
    i_sticksTotal -= int(float(i_choice)) #subtract number of sticks the player picked 
    if WinCheck(i_sticksTotal, i_curPlayer): #if player has won 
      i_curPlayer *= -1 #if player has not won, switch to -1 - the computer takes control - flip player
      node = Node(i_depth, i_curPlayer, i_sticksTotal) #create the tree tha algorithm is going to run on 
      bestChoice = -100 #hold 1 or 2, number of sticks 
      i_bestValue = -i_curPlayer * maxsize #store best value = starts off as the opposite amount of infinity 
      for i in range(len(node.children)): #iterate through the algorithm - compare two different choices 
          n_child = node.children[i]
          i_val = minmax(n_child, i_depth, -i_curPlayer)
          if (abs(i_curPlayer * maxsize -i_val) <= 
              abs(i_curPlayer * maxsize -i_bestValue)):
              i_bestValue = i_val
              bestChoice = i 
      bestChoice += 1
      print('computer chooses:' + str(bestChoice) + " based on value:" + str(i_bestValue))
      i_sticksTotal -= bestChoice #reduce stick total
      WinCheck(i_sticksTotal, i_curPlayer)
      i_curPlayer *= -1 #reverse player 