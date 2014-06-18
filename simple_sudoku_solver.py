"""
http://freepythontips.wordpress.com/2013/09/01/sudoku-solver-in-python/
"""

import sys

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

def r(a):
  i = a.find('x')
  if i == -1:
    #sys.exit(a)
    display(a)
    return

  excluded_numbers = set()
  for j in range(81):
    if same_row(i,j) or same_col(i,j) or same_block(i,j):
      excluded_numbers.add(a[j])

  for m in '123456789':
    if m not in excluded_numbers:
      r(a[:i]+m+a[i+1:])


def display(res):
    s = list(' '.join(res))
    s.append('\n')
    
    for i in range(17,len(s),18):
        s[i] = '\n'
        
    print ''.join(s)
    



if __name__ == '__main__':
  if len(sys.argv) == 2: # and len(sys.argv[1]) == 81:
    filename = sys.argv[1]
    f = open(filename)
    sudoku = ''
    for line in f.readlines():
        sudoku += line
        if len(sudoku) >= 162:
            sudoku = ''.join(sudoku.replace('\n','').replace(' ',''))
            r(sudoku)
            sudoku = ''
    f.close()

  else:
    print 'Usage: python sudoku.py puzzle'
    print 'where puzzle is an 81 char string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank'
