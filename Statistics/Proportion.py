def proportion(propList):
    try:
        result = 0
        num = 0
        for i in propList:
            if (i % 2) == 0:
                num = num + 1

            result = num / len(propList)
        return result
    except Exception as e:
        print("Error in Proportion", e)
        return 0
