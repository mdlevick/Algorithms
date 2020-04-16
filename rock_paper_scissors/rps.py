#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  all_poss = []

  def choice (update, iteration):
    if n == 0:
        all_poss.append(update)
        return
    for option in options:
      update.append(option)
      if iteration == n:
        all_poss.append(update.copy())
      else:
        choice(update, iteration + 1)
      update.pop()
  
  choice([], 1)
  
  return all_poss

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')