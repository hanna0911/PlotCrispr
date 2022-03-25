import xlrd
import json


data = xlrd.open_workbook('Nordic34.xlsx') # 打开excel表格
table = data.sheets()[0] # 通过索引顺序获取
nrows = table.nrows  # 获取总行数
ncols = table.ncols  # 获取总列数

Category = table.row_values(0) # 获取第一行值
# excel_id = table.col_values(0)  # 获取第一列值

sequences = []

# nrows = 2
row = 1
prev_excel_id = -1

while (row < nrows):
   
    content = table.row_values(row)
    
    sequence = {}  # 新的序列（通过excel_id识别） 
    sequence['excel_id'], sequence['seq_id'] = int(content[0]), content[1]
    sequence['CRISPR_start'], sequence['CRISPR_end'] = int(content[2]), int(content[3])
    prev_excel_id = int(content[0])

    proteins = []

    while(prev_excel_id == int(content[0])):

        protein = {}
        protein['protein_id'], protein['faa_id'] = content[12], content[13]
        protein['protein_start'], protein['protein_end'] = int(content[4]), int(content[5])
        protein['E_value'] = content[6]
        protein['distace_between_CRISPR_pro'] = int(content[7])
        protein['length'] = int(content[8])
        protein['anno_name'], protein['pfam_anno_name'], protein['function'] = content[9], content[10], content[11]

        proteins.append(protein)

        row = row + 1  # 下一行
        if(row >= nrows):
            break
        content = table.row_values(row)    

    sequence['proteins'] = proteins
    sequences.append(sequence)
    # row = row + 1
    

with open('Nordic34.json', 'w') as f:
    f.write(json.dumps(sequences))
