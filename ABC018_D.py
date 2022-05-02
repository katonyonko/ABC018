import io
import sys

_INPUT = """\
6
3 4 2 3 7
1 1 9
1 2 7
1 3 15
1 4 6
2 2 3
2 4 6
3 3 6
4 5 3 2 9
2 3 5
3 1 4
2 2 2
4 1 9
3 5 3
3 3 8
1 4 5
1 5 7
2 4 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,P,Q,R=map(int,input().split())
  ch=[]
  ans=0
  for i in range(R):
    x,y,z=map(int,input().split())
    x-=1; y-=1
    ch.append((x,y,z))
  for i in range(1<<N):
    tmp=[1 if (i>>j)&1==1 else 0 for j in range(N)]
    if sum(tmp)!=P: continue
    tmp2=[0]*M
    for j in range(R):
      x,y,z=ch[j]
      if tmp[x]==1:
        tmp2[y]+=z
    tmp2.sort(reverse=True)
    ans=max(ans,sum(tmp2[:Q]))
  print(ans)