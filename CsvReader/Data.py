def Data(data, string):
    dat = []
    for row in data.data:
        dat.append(int(row[string]))
    return dat
