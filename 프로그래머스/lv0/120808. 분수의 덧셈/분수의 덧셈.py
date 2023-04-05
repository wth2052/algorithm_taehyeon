#최대공약수
def GCD(n, n1):
    while(n1):
        n,n1=n1, n%n1
    return n



def solution(numer1, denom1, numer2, denom2):
    #분자
    numer = denom1 * numer2 + denom2 * numer1
    #분모
    denom = denom1 * denom2
    gcd = GCD(denom, numer)
    print(gcd)
    print(numer//gcd)
    print(denom//gcd)
    return [numer//gcd, denom//gcd]