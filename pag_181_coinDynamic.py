def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    return minCoins[change]


for i in range(1,500):
    change = i
    coinCount = [0]*(i+1)
    print(dpMakeChange([1,2,5,10,25], change, coinCount))