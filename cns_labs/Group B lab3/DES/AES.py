#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy


# In[2]:


SubByte = [
    ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
    ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
    ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
    ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
    ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
    ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
    ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
    ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
    ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
    ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
    ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
    ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
    ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
    ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
    ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
    ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
]
Inverse_SubByte = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

MixColumn = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
InverseMixColumn = [[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]]

d = dict( (j, (str(hex(x).split('x')[-1])+str(hex(y).split('x')[-1])).upper()) for x, i in enumerate(SubByte) for y, j in enumerate(i) )
#print(d)

for i in range(16):
    for j in range(16):
        m, n = SubByte[i][j][0], SubByte[i][j][1]
        x = int(m,16)
        y = int(n,16)
        Inverse_SubByte[x][y] = d[SubByte[i][j]]


# In[3]:


def hexadecimal1(x):
    x1 = ord(x)
    z = str(hex(x1)).split('x')
    if(len(z[1]) != 2):
        z[1] = '0'+z[1]
    return z[1].upper()


# In[4]:


def XOR(x, y):
    z = []
    for i in range(4):
        temp = str(hex(int(x[i],16)^int(y[i],16)).split('x')[-1]).upper()
        if(len(temp) != 2):
            temp = '0'+temp
        
        z.append(temp)
    return z


# In[5]:


def EntendKey(KEY):
    l1 = list(KEY)
    l2 = [hexadecimal1(i) for i in l1]
    #print(l2)
    roundKey = []
    roundKey.append(l2)
    #print(roundKey)
    RC = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']
    rc = [int(i,16) for i in RC]
    for i in range(10):
        w3 = [roundKey[-1][13], roundKey[-1][14], roundKey[-1][15], roundKey[-1][12]]
        subtituteByte = []

        for j in range(4):
            s1 = int(w3[j][0],16)
            s2 = int(w3[j][1],16)
            subtituteByte.append(SubByte[s1][s2])


        subtituteByte[0] = str(hex(int(subtituteByte[0],16)^int(rc[i]))).split('x')[-1].upper()

        if len(subtituteByte[0]) != 2:
            subtituteByte[0] = '0'+subtituteByte[0]

        #print(subtituteByte)
        w4 = XOR(roundKey[-1][0:4],subtituteByte)
        w5 = XOR(roundKey[-1][4:8], w4)
        w6 = XOR(roundKey[-1][8:12], w5)
        w7 = XOR(roundKey[-1][12:16], w6)
        w_final = w4 + w5 + w6 + w7
        roundKey.append(w_final)
    return roundKey


# In[6]:


def XOR1(x, y):
    z = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    for i in range(4):
        for j in range(4):
            temp = str(hex(int(x[i][j],16)^int(y[i][j],16)).split('x')[-1]).upper()
            if(len(temp) != 2):
                temp = '0'+temp

            z[i][j] = temp
    return z


# In[7]:


def left_shift(x):
    m = str(hex(int(x, 16)<<1)).split('x')[-1].upper()
    r = ''
    if(len(m)==3):
        m = str(hex(int(m,16)^283)).split('x')[-1].upper()
    if(len(m) != 2):
        m = '0'+m
    r = m[-2]+m[-1]
    return r

def hexadecimalXOR(x, y):
    z = str(hex(int(x, 16)^int(y, 16))).split('x')[-1].upper()
    if(len(z) != 2):
        z = '0'+z
    return z

def left_shift_AND_XOR(x):
    m = left_shift(x)
    n = hexadecimalXOR(m ,x)
    return n

def multiplication(x,y):
    
    z = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    for i in range(4):
        for j in range(4):
            m = '00'
            for k in range(4):
                if(x[i][k] == 2):
                    a = left_shift(y[k][j])
                    m = hexadecimalXOR(m,a)
                elif(x[i][k] == 1):
                    m = hexadecimalXOR(m, y[k][j])
                elif(x[i][k] == 3):
                    m = hexadecimalXOR(m, left_shift_AND_XOR(y[k][j]))
                elif(x[i][k] == 9):
                    a = left_shift(left_shift(left_shift(y[k][j])))
                    b = hexadecimalXOR(a,y[k][j])
                    m = hexadecimalXOR(m, b)
                    #print(m,a,b)
                elif(x[i][k] == 11):
                    a = left_shift(left_shift(left_shift(y[k][j])))
                    b = left_shift(y[k][j])
                    c = hexadecimalXOR(a, b)
                    d = hexadecimalXOR(c, y[k][j])
                    m = hexadecimalXOR(m, d)
                    #print(m,a,b,c,d)
                elif(x[i][k] ==13):
                    a = left_shift(left_shift(left_shift(y[k][j])))
                    b = left_shift(left_shift(y[k][j]))
                    c = hexadecimalXOR(a, b)
                    d = hexadecimalXOR(c, y[k][j])
                    m = hexadecimalXOR(m, d)
                    #print(m,a,b,c,d)
                elif(x[i][k] == 14):
                    a = left_shift(left_shift(left_shift(y[k][j])))
                    b = left_shift(left_shift(y[k][j]))
                    c = left_shift(y[k][j])
                    d = hexadecimalXOR(a, b)
                    e = hexadecimalXOR(c, d)
                    m = hexadecimalXOR(m, e)
                    #print(m,a,b,c,d,e)
            z[i][j] = m
    return z


# In[8]:


def encrypt(msg, roundKey):
    msg_list = list(msg)
    msg_list1 = [hexadecimal1(i) for i in msg_list]
    state_matrix = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    temp_key = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

    k = 0
    for i in range(4):
        for j in range(4):
            state_matrix[j][i] = msg_list1[k]
            k = k+1

    k = 0
    for i in range(4):
        for j in range(4):
            temp_key[j][i] = roundKey[0][k]
            k = k+1

    state_matrix = XOR1(state_matrix, temp_key)
    
    for i in range(10):

        # SubstitutionBytes
        for j in range(4):
            for k in range(4):
                m = int(state_matrix[j][k][0], 16)
                n = int(state_matrix[j][k][1], 16)
                state_matrix[j][k] =  SubByte[m][n]

        #print(state_matrix)

        # Shift Row
        temp = copy.deepcopy(state_matrix)

        for j in range(4):
            for k in range(4):
                state_matrix[j][k] = temp[j][(k+j)%4]

        #print(state_matrix)


        # Mix Column
        if(i != 9):
            state_matrix = multiplication(MixColumn, state_matrix)

        #print(state_matrix)

        # Round Key
        z = [
            [roundKey[i+1][0], roundKey[i+1][4], roundKey[i+1][8], roundKey[i+1][12]],
            [roundKey[i+1][1], roundKey[i+1][5], roundKey[i+1][9], roundKey[i+1][13]],
            [roundKey[i+1][2], roundKey[i+1][6], roundKey[i+1][10], roundKey[i+1][14]],
            [roundKey[i+1][3], roundKey[i+1][7], roundKey[i+1][11], roundKey[i+1][15]],
        ]
        state_matrix = XOR1(state_matrix, z)
        #print(state_matrix)

    cipherText = ''
    for i in range(4):
        for j in range(4):
            cipherText += state_matrix[j][i]

    return cipherText


# In[9]:


def msg_Conversion(x):
    m = int(x,16)
    return chr(m)


# In[10]:


def decrypt(cipherText, roundKey):
    state_matrix = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    #print(cipherText)
    for i in range(4):
        for j in range(4):
            state_matrix[j][i] = cipherText[2*j+8*i:2*j+8*i+2]
    #print(state_matrix)
    i = 9
    # Round Key
    z = [
        [roundKey[i+1][0], roundKey[i+1][4], roundKey[i+1][8], roundKey[i+1][12]],
        [roundKey[i+1][1], roundKey[i+1][5], roundKey[i+1][9], roundKey[i+1][13]],
        [roundKey[i+1][2], roundKey[i+1][6], roundKey[i+1][10], roundKey[i+1][14]],
        [roundKey[i+1][3], roundKey[i+1][7], roundKey[i+1][11], roundKey[i+1][15]],
    ]
    state_matrix = XOR1(state_matrix, z)

    #print(state_matrix)

    for i in range(8, -2, -1):

        # Shift Row
        temp = copy.deepcopy(state_matrix)

        for j in range(4):
            for k in range(4):
                state_matrix[j][k] = temp[j][(4+k-j)%4]

        #print(state_matrix)


        # SubstitutionBytes
        for j in range(4):
            for k in range(4):
                m = int(state_matrix[j][k][0], 16)
                n = int(state_matrix[j][k][1], 16)
                state_matrix[j][k] =  Inverse_SubByte[m][n]

        #print(state_matrix)

        # Round Key
        z = [
            [roundKey[i+1][0], roundKey[i+1][4], roundKey[i+1][8], roundKey[i+1][12]],
            [roundKey[i+1][1], roundKey[i+1][5], roundKey[i+1][9], roundKey[i+1][13]],
            [roundKey[i+1][2], roundKey[i+1][6], roundKey[i+1][10], roundKey[i+1][14]],
            [roundKey[i+1][3], roundKey[i+1][7], roundKey[i+1][11], roundKey[i+1][15]],
        ]
        state_matrix = XOR1(state_matrix, z)
        #print(state_matrix)

        # Mix Column
        if(i != -1):
            state_matrix = multiplication(InverseMixColumn, state_matrix)

        #print(state_matrix)
        
    plainText_list = list()

    for i in range(4):
        for j in range(4):
            plainText_list.append(state_matrix[j][i])

    #print(plainText_list)
    LL1 = [msg_Conversion(i) for i in plainText_list]
    #print(LL1)
    plainText = ''.join(LL1)
    return plainText


# In[11]:


#KEY = 'Thats my Kung Fu'
KEY = input('Enter a Key of 128 bits:')
#msg = 'Two One Nine Two'
msg = input('Enter the msg which needs to be encrypted:')
roundKey = EntendKey(KEY)
cipherText = encrypt(msg, roundKey)
print(cipherText)
plainText = decrypt(cipherText, roundKey)
print(plainText)

