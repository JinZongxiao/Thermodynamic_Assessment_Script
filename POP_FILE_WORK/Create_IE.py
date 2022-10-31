# -*- coding = utf-8 -*-
# @Time : 24/10/2022 下午3:20
# @Author : Sinclair
# @File : Create_IE.py
# @Software : PyCharm

data = []
#input file shout be enter into this for
for line in open("TDB_dir/test_inva.txt", "r", encoding='utf-8'):
    #index = line.find(':')+1
    #line = line[index:]
    line = line.split(':')[1]
    #print(line)
    if(line != '\n'):
        line = line.strip('\n')
        data.append(line)
print(data)

if data[0] == 'cong':
    Phase1 = data[1]
    Phase2 = data[2]
    Phase3 = ''
    condition_Congruent = data[4]
    EXP_T = data[3]
    EXP_1 = data[5]
    line1_const = 'Create_New_Equilibrium @@,1' + '\n'
    line2_const = 'Change_status Phase *=S' + '\n'
    line3 = 'Change_status Phase ' + Phase1 + Phase2 + Phase3 + '=Fix 1' + '\n'
    line4 = 'Set_Condition P=P0' + '\n'
    line5 = 'Set_Condition' + condition_Congruent + '\n'
    line6 = 'Experiment T=' + EXP_T + '\n'
    line7 = 'Experiment' + EXP_1 + '\n'
    #output path
    path = 'D:\\pythonProject\\CuTiProject\\TDB_dir\\out.txt'
    with open(path,'a+',encoding='utf-8') as f:
        f.write(line1_const)
        f.write(line2_const)
        f.write(line3)
        f.write(line4)
        f.write(line5)
        f.write(line6)
        f.write(line7)
        f.close()
else:
    Phase1 = data[1]
    Phase2 = data[2]
    Phase3 = data[3]
    EXP_T = data[4]
    EXP_1 = data[5]
    EXP_2 = data[6]
    EXP_3 = data[7]
    line1_const = 'Create_New_Equilibrium @@,1' + '\n'
    line2_const = 'Change_status Phase *=S' + '\n'
    line3 = 'Change_status Phase ' + Phase1 + Phase2 + Phase3 + '=Fix 1' + '\n'
    line4 = 'Set_Condition P=P0' + '\n'
    line5 = 'Experiment T=' + EXP_T + '\n'
    line6 = 'Experiment' + EXP_1 + '\n'
    line7 = 'Experiment' + EXP_2 + '\n'
    line8 = 'Experiment' + EXP_3 + '\n'
    #output path
    path = 'D:\\pythonProject\\CuTiProject\\TDB_dir\\out_inva.txt'
    with open(path,'a+',encoding='utf-8') as f:
        f.write(line1_const)
        f.write(line2_const)
        f.write(line3)
        f.write(line4)
        f.write(line5)
        f.write(line6)
        f.write(line7)
        f.write(line8)
        f.close()
