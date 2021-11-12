class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        AIn = False
        BIn = False
        Aindex = 0
        Bindex = 0
        Aflat = []
        for aVal in A:
            Aflat.append((aVal[0],True))
            Aflat.append((aVal[1],False))
        Bflat = []
        for bVal in B:
            Bflat.append((bVal[0],True))
            Bflat.append((bVal[1],False))
        
        mergeAry = []
        while Aindex < len(Aflat) and Bindex < len(Bflat):
            if Aflat[Aindex][0] == Bflat[Bindex][0]:
                if Aflat[Aindex][1]:
                    mergeAry.append((Aflat[Aindex][0],True,'A'))
                    mergeAry.append((Bflat[Bindex][0],Bflat[Bindex][1],'B'))
                else:
                    mergeAry.append((Bflat[Bindex][0],Bflat[Bindex][1],'B'))
                    mergeAry.append((Aflat[Aindex][0],Aflat[Aindex][1],'A'))
                Aindex += 1
                Bindex += 1
                continue
                
            if Aflat[Aindex][0] < Bflat[Bindex][0]:
                if Aflat[Aindex][1]:
                    mergeAry.append((Aflat[Aindex][0],True,'A'))
                else:
                    mergeAry.append((Aflat[Aindex][0],False,'A'))
                Aindex+=1
            else:
                if Bflat[Bindex][1]:
                    mergeAry.append((Bflat[Bindex][0],True,'B'))
                else:
                    mergeAry.append((Bflat[Bindex][0],False,'B'))
                Bindex += 1
        aActive = False
        bActive = False
        start = None
        res = []
        
        for val in mergeAry:
            if val[2] == 'A':
                if val[1]:
                    aActive = True
                else:
                    aActive = False
            else:
                if val[1]:
                    bActive = True
                else:
                    bActive = False
            if aActive and bActive:
                start = val[0]
            else:
                if start != None:
                    res.append((start,val[0]))
                start = None
        
        return res
                
        
                
        