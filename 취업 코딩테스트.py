# 백준 2630 색종이 만들기
import sys
input=sys.stdin.readline
 
a=input().rstrip()

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)] 

print(paper)