import numpy as np
import cv2 as cv

def amf(gray,row,col,Kmax):
    M,N = gray.shape
    Zxy=gray[row,col]
    ksize=3
    padding=ksize//2
    while ksize<Kmax:
        sub=gray[max(0,row-padding):min(N,row+padding+1),max(0,col-padding):min(M,col+padding+1)]
        Zmed=np.median(sub)
        Zmax=np.max(sub)
        Zmin=np.min(sub)
        if Zmin<Zmed<Zmax:
            if Zmin<Zxy<Zmax:
                return Zxy
            else:
                return Zmed
        else:
            ksize+=2
        return ksize



def AMFilter(gray,Kmax):
    N,M=gray.shape
    out=np.zeros_like(gray)
    for row in range(N):
        for col in range(M):
            out[row,col]=amf(gray,row,col,Kmax)
    return out