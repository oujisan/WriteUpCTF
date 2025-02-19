flag = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2'
fix_flag = ''.join(flag[i+2] + flag[i:i+2] for i in range(0,len(flag),3))
print(fix_flag)