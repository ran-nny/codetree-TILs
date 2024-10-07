s = input().split()

string = s[0]
string_list = list(string)
string_len = len(string)
query_cnt = int(s[1]) # 질의 개수

for _ in range(query_cnt):
    query_set = input().split()
    query_num = int(query_set[0])
    # 첫번째 쿼리
    if query_num == 1: 
        idx_1 = int(query_set[1])-1
        idx_2 = int(query_set[2])-1

        # idx1문자와 idx2문자 교환 후 출력
        tmp = string_list[idx_1]
        string_list[idx_1] = string_list[idx_2]
        string_list[idx_2] = tmp

        string = ''.join(string_list)
        print(string)

    # 두번째 쿼리
    else:
        s1_change = query_set[1]
        s2 = query_set[2]

        for i in range(string_len):
            if string_list[i] == s1_change:
                string_list[i] = s2
        string = ''.join(string_list)
        print(string)