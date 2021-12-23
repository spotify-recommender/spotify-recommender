def normalize(data):
    newdata = []
    for i in range(len(data)):
        if i == 2:
            newdata.append(max(0, (min(data[i], 7.234) - (-60.0)) / (7.234 - (-60.0))))
        elif i == 8:
            newdata.append(
                max(
                    0,
                    (min(data[i], 248.93400000000003) - 0.0)
                    / (248.93400000000003 - 0.0),
                )
            )
        elif i == 9:
            newdata.append(max(0, (min(data[i], 6061090) - 1000) / (6061090 - 1000)))
        else:
            newdata.append(data[i])
    return newdata
