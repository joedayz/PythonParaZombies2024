print('value\tfloor\tceiling\teven-rounded:')

for tentimes in range(30,47):
    c = tentimes / 10
    print(c,'\t',round(c-0.49),'\t',round(c+0.49),'\t',round(c))