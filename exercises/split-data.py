
def write_file(filename, data, header):

    with open(filename, 'r') as fr:
        look_data = fr.read()
    if look_data == "":
        with open(filename, 'w') as fw:
            fw.write('{header} \n{line}\n{data}'.format(
                    data=data,
                    line='='*12,
                    header=header
                ))
    else:
        with open(filename, 'a') as fa:
            fa.write(f'\n{data}')


with open('data.txt', 'r') as f:
  data = f.read();

data_list = data.split('\n')
count = 1
for phrase in data_list:
    if phrase != "":
        words = phrase.split(',')
        print(words)
        name = words[0]
        surname1 = words[1]
        surname2 = words[2]
        
        write_file('name.txt', name, 'Names')
        write_file('surname1.txt', surname1, 'Surname1')
        write_file('surname2.txt', surname2, 'Surname2')
        
        print(f'writted {count}')
        count += 1
        
