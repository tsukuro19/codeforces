def mini_time(books,time,n):
    sum_read=0
    ans,current=0,0
    if sum(books)==time:
        return len(books)
    else:
        for i in range(n):
            while current<n and sum_read+books[current]<=time:
                sum_read+=books[current]
                current+=1
            ans=max(ans,current-i)
            sum_read-=books[i]
        return ans

n,time=map(int,input().split())
books=list(map(int,input().split()))
print(mini_time(books,time,n))
