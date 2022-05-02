import io
import sys

_INPUT = """\
6
abcdef
2
3 5
1 4
redcoat
3
1 7
1 2
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=list(input())
  N=int(input())
  for i in range(N):
    l,r=map(int,input().split())
    tmp=S[l-1:r][::-1].copy()
    for i in range(l-1,r):
      S[i]=tmp[i-l+1]
  print(*S,sep='')