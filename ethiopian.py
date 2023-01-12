# 굿모닝~~ 

def ehiopian():
    answer=0 
    a,b=map(int,input("숫자 두개를 띄어서 입력하세요:").split())
    while(a>0):
        if a%2!=0:
            answer+=b
        a=a//2
        b=b*2
    print(answer)
    return answer


if __name__ == "__main__":
    ehiopian()
