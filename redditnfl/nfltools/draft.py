#!/usr/bin/env python

FORFEITED = 'X'
MOVED = 'M'
MOVED_TO = 'm'
COMP = 'c'
JC2A = 'j'
UNKNOWN = '?'

PICK_FLAGS = (UNKNOWN, FORFEITED, MOVED, MOVED_TO, COMP, JC2A)

def parsedrafts(s):
    drafts = {}
    for ds in s.split("---"):
        ds = ds.strip().split("\n")
        year = int(ds[0])
        ovr = 0
        draft = []
        for rs in ds[1:]:
            round_no, picks = rs.split(": ")
            rnd = []
            for ps in picks.split(","):
                flag = None
                if ps[-1] in PICK_FLAGS:
                    flag = ps[-1]
                    ps = ps[:-1]
                pick = int(ps)
                if flag is None or flag not in (FORFEITED, MOVED):
                    ovr += 1
                    rnd.append((pick, flag, ovr))
                else:
                    rnd.append((pick, flag, None))
            draft.append(rnd)
        drafts[year] = draft
    return drafts

def overall(year, t_rnd, t_pick):
    if year not in drafts:
        return -1
    draft = drafts[year]
    overall = 0
    rnd_no = 0
    for rnd in draft:
        rnd_no += 1
        for pick, flag, ovr in rnd:
            if flag is None or flag not in (FORFEITED, MOVED):
                overall += 1
            if rnd_no == t_rnd and pick == t_pick:
                return overall
    
def pick_type(year, rnd, pick):
    if year not in drafts:
        raise Exception("I don't know about draft %s" % year)
    if pick < 1 or rnd < 1:
        return UNKNOWN
    try:
        return drafts[year][rnd-1][pick-1][1]
    except Exception:
        return UNKNOWN

def round_pick(year, ovr):
    if year not in drafts:
        return -1
    draft = drafts[year]
    rnd_no = 0
    for rnd in draft:
        rnd_no += 1
        for pick, flag, _ in rnd:
            if overall(year, rnd_no, pick) == ovr:
                return rnd_no, pick




drafts = parsedrafts("""
2017
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c,43c
4: 1,2,3,4,5,6,7,8,9,10,11X,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32c,33c,34m,35c,36c,37c,38c
5: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26X,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27X,28,29,30,31,32,33c,34c,35c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c
---
2018
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c
4: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c
5: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c,43c,44c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c
---
2019
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7X,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c
4: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c
5: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14X,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c
---
2020
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c
4: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c
5: 1,2,3,4,5,6,7,8X,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c
---
2021
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7,8,9,10,11,12,13X,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39j,40j,41j,42j
4: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c
5: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c,43c,44c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14X,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
---
2022
1: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
2: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
3: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35j,36j,37j,38j,39j,40j,41j
4: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c
5: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c
6: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17X,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c,42c,43c
7: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33c,34c,35c,36c,37c,38c,39c,40c,41c
""")

if __name__ == "__main__":
    assert overall(2017, 1, 1) == 1
    assert overall(2017, 2, 1) == 33
    assert overall(2017, 3, 1) == 65
    assert overall(2017, 4, 1) == 108
    assert overall(2017, 4, 13) == 119
    assert overall(2017, 4, 35) == 141
    assert overall(2017, 5, 1) == 145
    assert overall(2017, 5, 41) == 184
    assert overall(2017, 6, 1) == 185
    assert overall(2017, 7, 1) == 219
    assert overall(2017, 6, 26) == 210
    assert overall(2017, 6, 28) == 211
    assert overall(2017, 6, 35) == 218

    assert pick_type(2017, 5, 0) == UNKNOWN
    assert pick_type(2017, 5, 1) == None
    assert pick_type(2017, 5, 25) == None
    assert pick_type(2017, 5, 26) == FORFEITED
    assert pick_type(2017, 5, 27) == None
    assert pick_type(2017, 5, 32) == None
    assert pick_type(2017, 5, 33) == COMP
    assert pick_type(2017, 5, 41) == COMP
    assert pick_type(2017, 5, 42) == UNKNOWN

    assert round_pick(2017, 1) == (1,1)
    assert round_pick(2017, 32) == (1,32)

    assert round_pick(2017, 33) == (2,1)
    assert round_pick(2017, 64) == (2,32)

    assert round_pick(2017, 65) == (3,1)
    assert round_pick(2017, 96) == (3,32)
    assert round_pick(2017, 97) == (3,33)
    assert round_pick(2017, 107) == (3,43)

    assert round_pick(2017, 108) == (4,1)
    assert round_pick(2017, 117) == (4,10)
    assert round_pick(2017, 118) == (4,12)
    assert round_pick(2017, 128) == (4,22)
    assert round_pick(2017, 129) == (4,23)
    assert round_pick(2017, 137) == (4,31)
    assert round_pick(2017, 144) == (4,38)

    assert round_pick(2017, 145) == (5,1)
    assert round_pick(2017, 169) == (5,25)
    assert round_pick(2017, 170) == (5,27)
    assert round_pick(2017, 175) == (5,32)
    assert round_pick(2017, 176) == (5,33)
    assert round_pick(2017, 184) == (5,41)

    assert round_pick(2017, 185) == (6,1)
    assert round_pick(2017, 210) == (6,26)
    assert round_pick(2017, 211) == (6,28)
    assert round_pick(2017, 215) == (6,32)
    assert round_pick(2017, 216) == (6,33)
    assert round_pick(2017, 218) == (6,35)

    assert round_pick(2017, 219) == (7,1)
    assert round_pick(2017, 250) == (7,32)
    assert round_pick(2017, 251) == (7,33)
    assert round_pick(2017, 253) == (7,35)

    assert overall(2019, 7, 40) == 254
    assert pick_type(2019, 3, 7) == FORFEITED
    assert pick_type(2019, 3, 33) == COMP
    assert pick_type(2019, 3, 40) == UNKNOWN
    assert pick_type(2019, 4, 1) == None

    assert pick_type(2020, 5, 8) == FORFEITED
    assert len(drafts[2020][0]) == 32
    assert len(drafts[2020][1]) == 32
    assert len(drafts[2020][2]) == 42
    assert len(drafts[2020][3]) == 40
    assert len(drafts[2020][4]) == 34
    assert len(drafts[2020][5]) == 35
    assert len(drafts[2020][6]) == 41
    assert overall(2020, 1, 1) == 1
    assert overall(2020, 2, 1) == 33
    assert overall(2020, 3, 1) == 65
    assert overall(2020, 4, 1) == 107
    assert overall(2020, 5, 1) == 147
    assert overall(2020, 6, 1) == 180
    assert overall(2020, 7, 1) == 215
    assert sum([sum([1 for pick in rd if pick[1] not in (FORFEITED, MOVED)]) for rd in drafts[2020]]) == 255

    assert pick_type(2021, 3, 39) == JC2A
    assert pick_type(2021, 7, 14) == FORFEITED
    assert pick_type(2021, 3, 13) == FORFEITED
    assert len(drafts[2021][0]) == 32
    assert len(drafts[2021][1]) == 32
    assert len(drafts[2021][2]) == 42
    assert len(drafts[2021][3]) == 39
    assert len(drafts[2021][4]) == 40
    assert len(drafts[2021][5]) == 44
    assert len(drafts[2021][6]) == 32
    assert overall(2021, 1, 1) == 1
    assert overall(2021, 2, 1) == 33
    assert overall(2021, 3, 1) == 65
    assert overall(2021, 4, 1) == 106
    assert overall(2021, 5, 1) == 145
    assert overall(2021, 6, 1) == 185
    assert overall(2021, 7, 1) == 229
    assert sum([sum([1 for pick in rd if pick[1] not in (FORFEITED, MOVED)]) for rd in drafts[2021]]) == 259

    assert pick_type(2022, 3, 35) == JC2A
    assert pick_type(2022, 6, 17) == FORFEITED
    assert len(drafts[2022][0]) == 32
    assert len(drafts[2022][1]) == 32
    assert len(drafts[2022][2]) == 41
    assert len(drafts[2022][3]) == 38
    assert len(drafts[2022][4]) == 36
    assert len(drafts[2022][5]) == 43
    assert len(drafts[2022][6]) == 41
    assert overall(2022, 1, 1) == 1
    assert overall(2022, 2, 1) == 33
    assert overall(2022, 3, 1) == 65
    assert overall(2022, 4, 1) == 106
    assert overall(2022, 5, 1) == 144
    assert overall(2022, 6, 1) == 180
    assert overall(2022, 7, 1) == 222
    assert sum([sum([1 for pick in rd if pick[1] not in (FORFEITED, MOVED)]) for rd in drafts[2022]]) == 262

    for year in drafts:
        assert len(drafts[year]) == 7
