def addUnique(baseList,otherlist):
    auxDict=dict.fromkeys(baseList)
    for item in otherlist:
        if item not in auxDict:
            baseList.append(item)
            auxDict[item]=None