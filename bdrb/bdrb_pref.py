def generate_output_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as in_file:
        team_names = [line.strip() for line in in_file]

    with open(output_file_path, 'w') as out_file:
        out_file.write('teamNameItems: [\n')
        for name in team_names:
            out_file.write('    {\n')
            out_file.write(f'      team_name: \'{name}\',\n')
            out_file.write('      team_id: null,\n')
            out_file.write('    },\n')
        out_file.write('],\n')

# ファイルのパスを指定します。適宜変更してください。
input_file_path = 'bdrb/in.txt'
output_file_path = 'bdrbout.txt'
generate_output_file(input_file_path, output_file_path)
