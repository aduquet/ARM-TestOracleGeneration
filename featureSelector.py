import pandas as pd
import glob as gl
import os
import pathlib

import warnings

warnings.filterwarnings('ignore')


def saveFile(df, file_out):
    df.to_csv(file_out)
    print('\n ***  Data is saved in *** \n', file_out)


def meth(df):
    df_meth = df.copy()
    df_meth['push'] = 'none'
    df_meth['pop'] = 'none'
    df_meth['clear'] = 'none'

    df_meth['push_p'] = 'none'
    df_meth['pop_p'] = 'none'
    df_meth['clear_p'] = 'none'

    for index, row in df.iterrows():
        method_call = row['calledMethod']
        method_call_p = row['calledMethod_p']
        if method_call == 'push':
            df_meth.at[index, 'push'] = row['pushInput']

        if method_call == 'pop':
            df_meth.at[index, 'pop'] = row['peek_obj_type']

        if method_call == 'clear':
            df_meth.at[index, 'clear'] = 'clear'

        if method_call_p == 'push':
            df_meth.at[index, 'push_p'] = row['pushInput_p']

        if method_call_p == 'pop':
            df_meth.at[index, 'pop_p'] = row['peek_obj_type_p']

        if method_call_p == 'clear':
            df_meth.at[index, 'clear_p'] = 'clear'

    return df_meth


def meth2(df):
    df_meth2 = df.copy()
    df_meth2['push'] = 'FALSE'
    df_meth2['pop'] = 'FALSE'
    df_meth2['clear'] = 'FALSE'

    df_meth2['push_p'] = 'FALSE'
    df_meth2['pop_p'] = 'FALSE'
    df_meth2['clear_p'] = 'FALSE'

    for index, row in df.iterrows():
        method_call = row['calledMethod']
        method_call_p = row['calledMethod_p']

        if method_call == 'push':
            df_meth2.at[index, 'push'] = 'TRUE'

        if method_call == 'pop':
            df_meth2.at[index, 'pop'] = 'TRUE'

        if method_call == 'clear':
            df_meth2.at[index, 'clear'] = 'TRUE'

        if method_call_p == 'push':
            df_meth2.at[index, 'push_p'] = 'TRUE'

        if method_call_p == 'pop':
            df_meth2.at[index, 'pop_p'] = 'TRUE'

        if method_call_p == 'clear':
            df_meth2.at[index, 'clear_p'] = 'TRUE'

    return df_meth2


def fs_6(df, file_out, path):
    columName = list(df.keys())
    if 'diff' in columName:
        df = df[["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "diff"]]
    else:
        df = df[["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear"]]

    name = path + '\\' + file_out
    saveFile(df, name)


def fs_7(df, file_out, path):
    columName = list(df.keys())
    if 'diff' in columName:
        df = df[["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'size_p', "diff"]]
    else:
        df = df[["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'size_p']]

    name = path + '\\' + file_out
    saveFile(df, name)


def fs_8(df, file_out, path):
    columName = list(df.keys())
    if 'diff' in columName:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'calledMethod',
             'size_p', "diff"]]
    else:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'calledMethod',
             'size_p']]

    name = path + '\\' + file_out
    saveFile(df, name)


def fs_12(df, file_out, path):
    columName = list(df.keys())
    if 'diff' in columName:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p", "isEmpty_p",
             "peek_obj_type_p", "push_p", "pop_p", "clear_p", "diff"]]
    else:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p", "isEmpty_p",
             "peek_obj_type_p", "push_p", "pop_p", "clear_p"]]

    name = path + '\\' + file_out
    saveFile(df, name)


def fs_13(df, file_out, path):
    columName = list(df.keys())
    if 'diff' in columName:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p", "isEmpty_p",
             "peek_obj_type_p", "push_p", "pop_p", "clear_p", 'calledMethod', "diff"]]
    else:
        df = df[
            ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p", "isEmpty_p",
             "peek_obj_type_p", "push_p", "pop_p", "clear_p", 'calledMethod']]

    name = path + '\\' + file_out
    saveFile(df, name)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'direc', help=' *direc* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, direc, file_out):
        print('*** Reading Data ***')
        paths_f6 = str(pathlib.Path().absolute()) + '\\' + 'FS6'
        paths_f7 = str(pathlib.Path().absolute()) + '\\' + 'FS7'
        paths_f8 = str(pathlib.Path().absolute()) + '\\' + 'FS8'
        paths_f12 = str(pathlib.Path().absolute()) + '\\' + 'FS12'
        paths_f13 = str(pathlib.Path().absolute()) + '\\' + 'FS13'

        if not os.path.exists(paths_f6):
            os.mkdir('FS6')

        if not os.path.exists(paths_f7):
            os.mkdir('FS7')

        if not os.path.exists(paths_f8):
            os.mkdir('FS8')

        if not os.path.exists(paths_f12):
            os.mkdir('FS12')

        if not os.path.exists(paths_f13):
            os.mkdir('FS13')

        if direc == 'directory':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                name1 = file_out + '_A_' + name
                name2 = file_out + '_B_' + name
                df_meth = meth(df)
                df_meth2 = meth2(df)
                paths = str(pathlib.Path().absolute()) + '\\FS6'
                fs_6(df_meth, name1, path=paths)
                fs_6(df_meth2, name2, path=paths)

                paths = str(pathlib.Path().absolute()) + '\\FS7'
                fs_7(df_meth, name1, path=paths)
                fs_7(df_meth2, name2, path=paths)

                paths = str(pathlib.Path().absolute()) + '\\FS8'
                fs_8(df_meth, name1, path=paths)
                fs_8(df_meth2, name2, path=paths)

                paths = str(pathlib.Path().absolute()) + '\\FS12'
                fs_12(df_meth, name1, path=paths)
                fs_12(df_meth2, name2, path=paths)

                paths = str(pathlib.Path().absolute()) + '\\FS13'
                fs_13(df_meth, name1, path=paths)
                fs_13(df_meth2, name2, path=paths)


        else:
            df = pd.read_csv(file_in, index_col=0)
            name1 = file_out + 'A_' + 'No_modified.csv'
            name2 = file_out + 'B_' + 'No_modified.csv'
            df_meth = meth(df)
            df_meth2 = meth2(df)
            paths = str(pathlib.Path().absolute()) + '\\FS6'
            fs_6(df_meth, name1, path=paths)
            fs_6(df_meth2, name2, path=paths)

            paths = str(pathlib.Path().absolute()) + '\\FS7'
            fs_7(df_meth, name1, path=paths)
            fs_7(df_meth2, name2, path=paths)

            paths = str(pathlib.Path().absolute()) + '\\FS8'
            fs_8(df_meth, name1, path=paths)
            fs_8(df_meth2, name2, path=paths)

            paths = str(pathlib.Path().absolute()) + '\\FS12'
            fs_12(df_meth, name1, path=paths)
            fs_12(df_meth2, name2, path=paths)

            paths = str(pathlib.Path().absolute()) + '\\FS13'
            fs_13(df_meth, name1, path=paths)
            fs_13(df_meth2, name2, path=paths)

            # paths = str(pathlib.Path().absolute()) + '\\FS3'
            # fs_1(df, file_out, path=paths)
            # paths = str(pathlib.Path().absolute()) + '\\FS4'
            # fs_2(df, file_out, path=paths)
            # paths = str(pathlib.Path().absolute()) + '\\FS8'
            # fs_3(df, file_out, path=paths)
            # paths = str(pathlib.Path().absolute()) + '\\FS9'
            # fs_4(df, file_out, path=paths)
            # paths = str(pathlib.Path().absolute()) + '\\FS10'
            # fs_5(df, file_out, path=paths)

main()
