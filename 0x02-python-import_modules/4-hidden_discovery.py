#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    temp = dir(hidden_4)
    for t in range(len(temp)):
        for t_2 in range(len(temp[t])):
            if (temp[t][t_2] == '_') & (temp[t][t_2 + 1] == '_'):
                break
            else:
                print(temp[t])
                break
