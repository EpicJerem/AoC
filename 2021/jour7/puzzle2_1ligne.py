c=[int(i)for i in open('i').readline().split(',')];print(min([sum([abs(i-p)*(abs(i-p)+1)//2 for i in c])for p in range(max(c))]))