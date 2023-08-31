n=int(input())
s=list(map(int,input().split()))
cnt1,cnt2,cnt3,cnt4=0,0,0,0
for i in s:
    if i==4:cnt4+=1
    elif i==1:cnt1+=1
    elif i==2:cnt2+=1
    else: cnt3+=1
ans=cnt4
ans+=cnt2//2
cnt2=cnt2%2
if cnt1<=cnt3:
    ans+=cnt1
    ans+=cnt2
    ans+=cnt3-cnt1
else:
    ans+=cnt3
    cnt1-=cnt3
    ans+=cnt1//4
    cnt1=cnt1%4
    rem=cnt1+cnt2*2
    if rem > 0:
	    ans += 1 if rem <= 4 else 2
print(ans)
      