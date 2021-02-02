list_parameters_cmg = ('*INCLUDE', 'INCLUDE', 'FILENAME INDEX-IN', 'FILENAMES      INDEX-IN', '*FILENAME *INDEX-IN', '*FILENAMES  *INDEX-IN', 'FILENAMES MAIN-RESULTS-IN','*FILENAMES *MAIN-RESULTS-IN','FILENAMES REWIND-IN','*FILENAMES *REWIND-IN')
list_parameters_cmg_aux = []
for param in list_parameters_cmg:
    if param.strip().count(' ') > 1:
        list_parameters_cmg_aux.append(param.strip().replace(' ', '', param.strip().count(' ')-1))
print(f'list: {list_parameters_cmg_aux}')
if len(list_parameters_cmg_aux) > 0:
    print('Ok')
'''
OutPut:
list: ['FILENAMES INDEX-IN', '*FILENAMES *INDEX-IN']
Ok
Process finished with exit code 0
'''
