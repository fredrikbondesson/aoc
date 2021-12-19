import util
import sys
import timeit

INPUT="""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


INPUT_LARGE="""11637517422274862853338597396444961841755517295286
13813736722492484783351359589446246169155735727126
21365113283247622439435873354154698446526571955763
36949315694715142671582625378269373648937148475914
74634171118574528222968563933317967414442817852555
13191281372421239248353234135946434524615754563572
13599124212461123532357223464346833457545794456865
31254216394236532741534764385264587549637569865174
12931385212314249632342535174345364628545647573965
23119445813422155692453326671356443778246755488935
22748628533385973964449618417555172952866628316397
24924847833513595894462461691557357271266846838237
32476224394358733541546984465265719557637682166874
47151426715826253782693736489371484759148259586125
85745282229685639333179674144428178525553928963666
24212392483532341359464345246157545635726865674683
24611235323572234643468334575457944568656815567976
42365327415347643852645875496375698651748671976285
23142496323425351743453646285456475739656758684176
34221556924533266713564437782467554889357866599146
33859739644496184175551729528666283163977739427418
35135958944624616915573572712668468382377957949348
43587335415469844652657195576376821668748793277985
58262537826937364893714847591482595861259361697236
96856393331796741444281785255539289636664139174777
35323413594643452461575456357268656746837976785794
35722346434683345754579445686568155679767926678187
53476438526458754963756986517486719762859782187396
34253517434536462854564757396567586841767869795287
45332667135644377824675548893578665991468977611257
44961841755517295286662831639777394274188841538529
46246169155735727126684683823779579493488168151459
54698446526571955763768216687487932779859814388196
69373648937148475914825958612593616972361472718347
17967414442817852555392896366641391747775241285888
46434524615754563572686567468379767857948187896815
46833457545794456865681556797679266781878137789298
64587549637569865174867197628597821873961893298417
45364628545647573965675868417678697952878971816398
56443778246755488935786659914689776112579188722368
55172952866628316397773942741888415385299952649631
57357271266846838237795794934881681514599279262561
65719557637682166874879327798598143881961925499217
71484759148259586125936169723614727183472583829458
28178525553928963666413917477752412858886352396999
57545635726865674683797678579481878968159298917926
57944568656815567976792667818781377892989248891319
75698651748671976285978218739618932984172914319528
56475739656758684176786979528789718163989182927419
67554889357866599146897761125791887223681299833479"""

def get_item_from(row_nr, col_nr, data):
    if row_nr < 0:
        return -1
    if col_nr < 0:
        return -1
    try:
        return data[row_nr][col_nr]
    except IndexError:
        return -1

def get_as_list_of_lists(data):
    rows = []
    for row in data:
        buf = []
        for nr in row:
            buf.append(int(nr))

        rows.append(buf)
    return rows

# data = list(map(int, INPUT2.split()))
def get_as_duplicated_list_of_lists(data):
    rows = [-1] * len(data)
    for row in data:
        buf = []
        for nr in row:
            buf.append(int(nr))

        rows.append(buf)
    return rows


def get_adjacents(xpos, ypos, visited, indata):
    xy_neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    res = []
    for idx, (x_delta, y_delta) in enumerate(xy_neighbours):
        #print(idx, x_delta, y_delta)
        # print(xpos, x_delta, ypos, y_delta)
        cost = get_item_from(xpos + x_delta, ypos + y_delta, indata)
        if cost != -1 and (xpos + x_delta, ypos + y_delta) not in visited:
            #node = f'{int(xpos + x_delta)},{int(ypos+ y_delta)}'
            res.append((xpos + x_delta, ypos+ y_delta, cost))

    return res


def get_min_dist_value(distance_value, visited):
    min_cost = sys.maxsize
    min_node = (None, None)
    for node, cost in distance_value.items():
        if node not in visited and cost < min_cost:
            min_cost = cost
            min_node = node

    return min_node, min_cost


def run(start_x, start_y, indata, expected):
    visited = set()
    # current_node = f'{start_x},{start_y}'
    distance_value = {}
    distance_value[(start_x, start_y)] = 0
    visit_node(start_x, start_y, visited, distance_value, indata)

    #print(f'visited={visited}')
    #print()
    #print(f'distance_value={distance_value}')
    #print()
    print(distance_value[(len(indata[0]) - 1, len(indata) - 1)])
    assert distance_value[(len(indata[0]) - 1, len(indata) - 1)] == expected


def visit_node(start_x, start_y, visited, distance_value, indata):
    #print(f'visit_node=({start_x},{start_y})')
    current_node = (start_x, start_y)
    visited.add(current_node)
    next_x = start_x
    next_y = start_y
    while len(visited) < len(indata) * len(indata[0]):

        current_node = (next_x, next_y)

        adjacents = get_adjacents(next_x, next_y, visited, indata)
        #print(f'adjacents={adjacents}')
        #print(f'visited={visited}')
        #print(f'distance_value={distance_value}')

        for adjacent in adjacents:
            x = adjacent[0]
            y = adjacent[1]
            cost = adjacent[2]
            node = (x, y)
            current_cost = distance_value[current_node]
            #print(f'current_node={current_node} current_cost={current_cost} node={node} cost={cost}')
            if distance_value.get(node) is not None:
                if distance_value.get(node) != current_cost + cost:
                    #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + str(node) + " " + str(distance_value[node]) + "->" + str(current_cost + cost))
                    # assert False
                    pass
            else:
                distance_value[node] = current_cost + cost

        (next_x, next_y), next_node_cost = get_min_dist_value(distance_value, visited)
        if next_x is not None and next_y is not None:
            current_node = (next_x, next_y)
            visited.add(current_node)
        else:
            assert False


def main():
    print('INPUT DATA')
    start = timeit.default_timer()
    rows = get_as_list_of_lists(INPUT.split('\n'))
    startx = 0
    starty = 0
    run(startx, starty, rows, 40)
    print(len(rows) * len(rows[0]))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print('Part 1')
    start = timeit.default_timer()
    data = util.read_data('2021/day15.txt')
    rows = get_as_list_of_lists(data)
    startx = 0
    starty = 0
    print(len(rows) * len(rows[0]))
    run(startx, starty, rows, 652)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print('Part 2')
    start = timeit.default_timer()
    rows = get_as_list_of_lists(INPUT_LARGE.split('\n'))
    startx = 0
    starty = 0
    run(startx, starty, rows, 315)
    print(len(rows) * len(rows[0]))
    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    main()
