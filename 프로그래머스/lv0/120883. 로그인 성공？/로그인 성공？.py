def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'