import datetime;
import math;
now=datetime.datetime.now();
x = now.year+now.month+now.day+now.hour+now.minute+now.second;

print("How many random numbers : ");
y = (int)(input());

print("Enter the lower bound : ");

l = (int)(input());

print("Enter the uper bound : ");

r = (int)(input());
z = 1;
cnt = 1;
while(cnt<=y):
    
    x = x * x + z;
    z = (int)(math.sqrt(cnt));
    m = x % r;
    if(m<l):
        m=m*m;
    if(m>=l and m<=r):
        print(m);
        cnt = cnt + 1;
        
        
