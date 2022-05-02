import io
import sys

_INPUT = """\
6
12
18
11
10
20
30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  score=[[int(input()),i] for i in range(3)]
  score.sort(reverse=True)
  for i in range(3):
    print([score[i][1] for i in range(3)].index(i)+1)