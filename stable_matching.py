#This problem was not automater for abritrary values of input size.

M = [[0, 1, 2, 3], [3, 1, 0, 2], [2, 1, 0, 3], [0, 1, 2, 3]]
W = [[3, 2, 1, 0], [0, 1, 2, 3], [2, 3, 1, 0], [2, 0, 3, 1]]



def stable_matching(M,W):
    m_proposed = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    m_matched = [0, 0, 0, 0]
    f = len(M[0])
    w_partners = [f,f,f,f]
    while m_matched != [1, 1, 1, 1]: 
                i = m_matched.index(0)
                for k in M[i]:
                    t = 'flag'
                    if m_proposed[i][k] != 1:
                        t = k
                        break
                if t == 'flag':
                    return w_partners
                
                if w_partners[t] == f:
                    w_partners[t] = i
                    m_matched[i] = 1
                    m_proposed[i][t] = 1
                else:
                    j = W[t].index(w_partners[t])
                    if W[t].index(i) >= W[t].index(j):
                        m_proposed[i][t] = 1
                    else:
                        m_matched[i] = 1
                        m_matched[w_partners[t]] = 0
                        w_partners[t] = i
                        m_proposed[i][t] = 1
    return w_partners         
         

A = stable_matching(M,W)
print(A)