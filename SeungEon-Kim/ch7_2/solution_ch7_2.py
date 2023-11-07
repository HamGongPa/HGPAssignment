# 파이썬 소수 모듈 primePy
# 코드 실행 전 터미널에서 pip3 install primePy 먼저 실행

from primePy import primes
 
print("100부터 1000까지 소수 리스트: ", primes.between(100,1000))
print("100부터 1000까지 소수의 개수: ", len(primes.between(100,1000)))