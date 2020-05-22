import math

def GiveGeoSeqElement (a1=2,factor=2, index=2):
    an = a1* pow(factor,index-1)
    return an


def GiveFactorForGeoSeq (an, a1):
    factor = an / a1
    return factor


def GiveSumOfEmementsGeoSeq(a1=2,factor=2, n=2):
    Sn = a1*((1-pow(factor,n))/(1-factor))
    return Sn
9o
