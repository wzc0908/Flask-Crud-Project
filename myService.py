import sqlite3 as sql


def partition(mydata, low, high, mypivot):
    pivot = mydata[high][mypivot]
    i = low - 1
    for j in range(low, high):
        if mydata[j][mypivot] > pivot:
            i += 1
            (mydata[i], mydata[j]) = (mydata[j], mydata[i])
    (mydata[i + 1], mydata[high]) = (mydata[high], mydata[i + 1])
    return i + 1


def quicksort(mydata, low, high, mypivot):
    if low < high:
        pi = partition(mydata, low, high, mypivot)
        quicksort(mydata, low, pi - 1, mypivot)
        quicksort(mydata, pi + 1, high, mypivot)


def worst_components_algo():
    with sql.connect("database.db") as con3:
        cur = con3.cursor()
        cur.execute(
            " SELECT * FROM componentTable")

        con3.commit()
        mydata = cur.fetchall()

        print(mydata)
        size = len(mydata)
        quicksort(mydata, 0, size - 1, 4)
        print('Sorted Array in Descending Order:')
        print(mydata[0:5])

        return mydata[0:5]
        con.close()


def most_used_algo():
    with sql.connect("database.db") as con3:
        cur = con3.cursor()
        cur.execute(
            " SELECT * FROM mappingTable")
        con3.commit()
        mydata = cur.fetchall()

        map_dict = {}
        for i in mydata:
            temp_keys = map_dict.keys()
            current_key = i[2]
            if current_key in temp_keys:
                map_dict[current_key] += 1
            else:
                map_dict[current_key] = 1

        map_list = []
        for component_name in map_dict.keys():
            map_list.append([component_name, map_dict[component_name]])

        print(map_list)
        size = len(map_list)
        quicksort(map_list, 0, size - 1, 1)
        print('Sorted Array in Descending Order:')
        print(map_list[0:5])

        return map_list[0:5]
        con.close()


def worst_manufacturer_algo():
    with sql.connect("database.db") as con3:
        cur = con3.cursor()
        cur.execute(
            " SELECT * FROM componentTable")
        con3.commit()

        mydata2 = cur.fetchall()
        print(mydata2)
        comp_dict = {}
        for i in mydata2:
            comp_keys = comp_dict.keys()
            manu_key = i[3]
            manu_value = i[4]
            if manu_key in comp_keys:
                comp_dict[manu_key] = {
                    'val': float(comp_dict[manu_key]['val']) + float(manu_value),
                    'count': comp_dict[manu_key]['count'] + 1
                }
            else:
                comp_dict[manu_key] = {
                    'val': float(manu_value),
                    'count': 1
                }

        print(comp_dict)
        avg_rate = {}
        for value in comp_dict.keys():
            avg_rate[value] = comp_dict[value]['val'] / comp_dict[value]['count']
        print(avg_rate)

        manu_list = []
        for i in avg_rate.keys():
            manu_list.append([i, avg_rate[i]])

        print(manu_list)
        size = len(manu_list)
        quicksort(manu_list, 0, size - 1, 1)
        print('Sorted Array in Descending Order:')
        print(manu_list[0:3])
        return manu_list[0:3]
        con.close()
