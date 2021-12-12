import timeit
from collections import defaultdict
import util


"""start-A
start-b
A-c
A-b
b-d
A-end
b-end

{'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'd': ['b'], 'end': ['A', 'b']}


['start', 'A', 'c', 'b', 'end']
['start', 'A', 'c', 'b', 'end']
['start', 'b', 'A', 'd', 'end']
['start', 'b', 'A', 'd', 'end']


start A c
 start A c A
  start A c A c -> går inte redan kört c
  start A c A b
   start A c A b A
    start A c A b A c -> går inte redan kört c
    start A c A b A b -> går inte redan kört b
    start A c A b A end
   start A c A b d
    start A c A b d b -> går inte redan kört b
   start A c A b end
  start A c A end  
start A b
 start A b A
  start A b A c
   start A b A c A
    start A b A c A c -> går inte redan kört c
    start A b A c A b -> går inte redan kört b
    start A b A c A end
  start A b A b -> går inte redan kört b
  start A b A end 
 start A b d
  start A b d b -> går inte redan kört b
 start A b end
start A end

start,b,A
 start,b,A,c
   start,b,A,c,A
    start,b,A,c,A,c -> går inte redan kört c
    start,b,A,c,A,b -> går inte redan kört b
    start,b,A,c,A,end
 start,b,A,b -> går inte redan kört b
 start,b,A,end
start,b,d
 start,b,d,b -> går inte redan kört b
start,b,end

====>

start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end  
start,A,b,A,c,A,end
start,A,b,A,end 
start,A,b,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
"""



INPUT_SMALL="""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

# 10 paths through this example cave system:
INPUT_SMALL_SOLUTION="""start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end"""


INPUT = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


# The 19 paths through it are as follows:
INPUT_SOLUTION="""
start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
"""

# 226 paths through it
INPUT_LARGE = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def traverse_part1(nodes, traversed, traversed_all, connections, traverse_func):
    for next_node in nodes:
        tt = traversed.copy()
        if next_node == 'end':
            tt.append('end')
            traversed_all.append(tt)

            #print('At end')
            #for t in traversed_all:
            #    print(t)
            continue
        elif next_node == 'start':
            assert False, "Should not get here"
        else:
            if next_node.islower() and next_node in tt:
                #print(f"{next_node} is lower and in traversed")
                continue
            
            # print(f'Adding {next_node} to traversed {traversed}')
            tt.append(next_node)
            #print(f'tt {tt}')
            traverse_func(connections[next_node], tt, traversed_all, connections, traverse_func)


def traverse_part2(nodes, traversed, traversed_all, connections, traverse_func):
    for next_node in nodes:
        tt = traversed.copy()
        if next_node == 'end':
            tt.append('end')
            traversed_all.append(tt)

            continue
        elif next_node == 'start':
            assert False, "Should not get here"
        else:
            if next_node.islower():
                
                all_lowers = [item for item in tt if item.islower()]
                count_ = all_lowers.count(next_node)
                if count_ > 0:
                    all_lowers.remove(next_node)
                possible = True
                for node in all_lowers:
                    if all_lowers.count(node) > 1:
                        possible = False

                if count_ == 0:
                    tt.append(next_node)
                    traverse_func(connections[next_node], tt, traversed_all, connections, traverse_func)
                elif possible and count_ == 1:
                    tt.append(next_node)
                    traverse_func(connections[next_node], tt, traversed_all, connections, traverse_func)
                
                continue
            
            tt.append(next_node)
            traverse_func(connections[next_node], tt, traversed_all, connections, traverse_func)


def run(in_data, expected_nr_of_traversals, traverse_func):
        connections = defaultdict(list)
        for connection in in_data:        
            node1, node2 = connection.split('-')[0:2]
            if node1 != 'end' and node2 != 'start':
                connections[node1].append(node2)
            if node1 != 'start' and node2 != 'end':
                connections[node2].append(node1)

        print(in_data)
        print(connections)

        done = False
        traversed_all = []

        for node in connections['start']:
            traversed = []
            traversed.append('start')
            traversed.append(node)
            next_nodes = connections[node]

            traverse_func(next_nodes, traversed, traversed_all, connections, traverse_func)

        print(f'nr of traversions: {len(traversed_all)}')
        assert expected_nr_of_traversals == len(traversed_all),\
              f"Expected {expected_nr_of_traversals} but got {len(traversed_all)}"


def main():
    start = timeit.default_timer()
    run(INPUT_SMALL.split('\n'), 10, traverse_part1)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run(INPUT.split('\n'), 19, traverse_part1)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run(INPUT_LARGE.split('\n'), 226, traverse_part1)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    rows = util.read_data('2021/day12.txt')
    run(rows, 5756, traverse_part1)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run(INPUT_SMALL.split('\n'), 36, traverse_part2)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run(INPUT.split('\n'), 103, traverse_part2)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run(INPUT_LARGE.split('\n'), 3509, traverse_part2)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    rows = util.read_data('2021/day12.txt')
    run(rows, 144603, traverse_part2)
    stop = timeit.default_timer()
    print('Time: ', stop - start)        


if __name__ == '__main__':
    main()
