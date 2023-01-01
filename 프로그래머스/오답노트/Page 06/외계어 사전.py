'''
spell	                 dic	                                            result
["p", "o", "s"]	        ["sod", "eocd", "qixm", "adio", "soo"]	            2
["z", "d", "x"]	        ["def", "dww", "dzx", "loveaw"]	                    1
["s", "o", "m", "d"]	["moos", "dzx", "smm", "sunmmo", "som"]	            2
'''
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2


# issubset : 부분집합 여부 확인
def solution(spell, dic):
    spell = set(spell) 
    
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2