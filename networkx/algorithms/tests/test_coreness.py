# test_coreness.py - unit tests for the coreness module
#
# Copyright 2010 Reya Group <http://www.reyagroup.com>.
# Copyright 2010 Alex Levenson <alex@isnotinvain.com>.
# Copyright 2015 NetworkX developers.
#
# This file is part of NetworkX.
#
# NetworkX is distributed under a BSD license; see LICENSE.txt for more
# information.
"""Unit tests for the :mod:`networkx.algorithms.coreness` module."""
from nose.tools import assert_greater
from scipy.stats.stats import pearsonr

import networkx as nx


def test_coreness():
    template = nx.DiGraph()
    G = nx.parse_edgelist(EDGELIST.split('\n'), create_using=template)
    expected = {'1': 0.000158324, '2': 0.242791444, '3': 0.28162086,
                '4': 0.187891737, '5': 0.02693647, '6': 0.086915143,
                '7': 0.202999592, '8': 0.009302279, '9': 0.132965162,
                '10': 0.13493374, '11': 0.078446053, '12': 0.063676365,
                '13': 0.250760615, '14': 0.295324355, '15': 0.194265738,
                '16': 0.249910161, '17': 0.15948914, '18': 0.160584778,
                '19': 0.233398184, '20': 0.009938824, '21': 0.002118818,
                '22': 0.206798032, '23': 0.221797511, '24': 0.1135149,
                '25': 0.100778475, '26': 0.116816998, '27': 0.156726494,
                '28': 0.017239759, '29': 0.054217927, '30': 0.170990765,
                '31': 0.118929863, '32': 0.26917401, '33': 0.001095971,
                '34': 0.128328308, '35': 0.196426332, '36': 0.140603051,
                '37': 0.056695089, '38': 0.000118299, '39': 0.121552378,
                '40': 0.09787029}
    expected = [v for k, v in sorted(expected.items())]
    actual = [v for k, v in sorted(nx.coreness(G).items())]
    r = pearsonr(actual, expected)[0]
    # The correlation should be very high, close to one.
    assert_greater(r, 0.99)


#: The edge list of a graph to test.
EDGELIST = """1 18
1 32
1 38
1 39
2 3
2 4
2 6
2 7
2 9
2 10
2 13
2 17
2 18
2 19
2 22
2 23
2 28
2 31
2 32
2 34
2 35
2 38
3 2
3 4
3 5
3 7
3 11
3 14
3 15
3 16
3 19
3 22
3 24
3 25
3 30
3 32
3 34
3 35
3 36
3 39
3 40
4 2
4 3
4 5
4 7
4 13
4 15
4 16
4 17
4 19
4 21
4 22
4 24
4 32
4 40
5 3
5 4
5 17
5 21
5 26
5 36
5 37
6 2
6 10
6 11
6 13
6 14
6 18
6 23
6 36
7 2
7 3
7 4
7 9
7 13
7 16
7 19
7 22
7 26
7 30
7 34
7 35
7 36
7 40
8 9
8 10
8 11
8 16
8 37
8 39
9 2
9 7
9 8
9 10
9 12
9 13
9 14
9 15
9 16
9 20
9 25
9 35
9 37
10 2
10 6
10 8
10 9
10 11
10 13
10 14
10 15
10 16
10 23
10 26
10 36
10 38
11 3
11 6
11 8
11 10
11 15
11 16
11 20
11 21
11 25
11 26
11 31
11 36
12 9
12 13
12 15
12 17
12 18
12 25
12 27
12 37
12 40
13 2
13 4
13 6
13 7
13 9
13 10
13 12
13 14
13 15
13 16
13 18
13 19
13 20
13 24
13 25
13 30
13 31
13 32
13 37
14 3
14 6
14 9
14 10
14 13
14 15
14 17
14 18
14 19
14 23
14 24
14 26
14 27
14 30
14 31
14 32
14 35
14 36
14 39
14 40
15 3
15 4
15 9
15 10
15 11
15 12
15 13
15 14
15 17
15 18
15 23
15 25
15 27
15 35
15 36
16 3
16 4
16 7
16 8
16 9
16 10
16 11
16 13
16 17
16 18
16 19
16 22
16 23
16 27
16 30
16 32
16 37
16 39
17 2
17 4
17 5
17 12
17 14
17 15
17 16
17 22
17 23
17 27
17 32
17 39
18 1
18 2
18 6
18 12
18 13
18 14
18 15
18 16
18 20
18 23
18 24
18 27
18 35
18 39
19 2
19 3
19 4
19 7
19 13
19 14
19 16
19 22
19 26
19 27
19 30
19 31
19 32
19 36
20 9
20 11
20 13
20 18
20 21
20 27
21 4
21 5
21 11
21 20
21 24
21 26
21 36
22 2
22 3
22 4
22 7
22 16
22 17
22 19
22 23
22 28
22 29
22 30
22 32
22 33
22 34
22 35
22 40
23 2
23 6
23 10
23 14
23 15
23 16
23 17
23 18
23 22
23 24
23 27
23 32
23 34
23 35
23 36
23 37
24 3
24 4
24 13
24 14
24 18
24 21
24 23
24 26
24 27
24 39
25 3
25 9
25 11
25 12
25 13
25 15
25 26
25 27
25 30
25 31
25 39
26 5
26 7
26 10
26 11
26 14
26 19
26 21
26 24
26 25
26 27
26 28
26 29
26 30
26 32
27 12
27 14
27 15
27 16
27 17
27 18
27 19
27 20
27 23
27 24
27 25
27 26
27 36
27 37
27 39
28 2
28 22
28 26
28 29
28 34
28 40
29 22
29 26
29 28
29 30
29 34
29 35
29 36
29 39
29 40
30 3
30 7
30 13
30 14
30 16
30 19
30 22
30 25
30 26
30 29
30 31
30 32
31 2
31 11
31 13
31 14
31 19
31 25
31 30
31 32
31 35
32 1
32 2
32 3
32 4
32 13
32 14
32 16
32 17
32 19
32 22
32 23
32 26
32 30
32 31
32 34
32 35
32 39
33 22
33 34
33 40
34 2
34 3
34 7
34 22
34 23
34 28
34 29
34 32
34 33
34 35
34 36
34 40
35 2
35 3
35 7
35 9
35 14
35 15
35 18
35 22
35 23
35 29
35 31
35 32
35 34
35 40
36 3
36 5
36 6
36 7
36 10
36 11
36 14
36 15
36 19
36 21
36 23
36 27
36 29
36 34
37 5
37 8
37 9
37 12
37 13
37 16
37 23
37 27
37 39
38 1
38 2
38 10
39 1
39 3
39 8
39 14
39 16
39 17
39 18
39 24
39 25
39 27
39 29
39 32
39 37
40 3
40 4
40 7
40 12
40 14
40 22
40 28
40 29
40 33
40 34
40 35"""
