import os
import pathlib
import pandas as pd
import numpy as np
import glob as gl
import warnings

warnings.filterwarnings('ignore')


def saveFile(df, file_out):
    df.to_csv(file_out)
    print('\n *** Encode Data is saved in *** \n', file_out)


def encoder(df):
    """
    Encode the Stack dataframe features to make is readable after the rule mining
    """
    data = df.copy()
    columName = list(df.keys())

    if 'diff' in columName:

        fs6 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "diff"]
        if fs6 == columName:
            data['size'] = df['size'].astype(float)
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' or n == 'diff':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs7 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'size_p', "diff"]
        if fs7 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' or n == 'diff':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs8 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'calledMethod',
               'size_p', "diff"]
        if fs8 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['calledMethod'] = df['calledMethod'].astype(str).str.lower()
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' or n == 'diff':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs12 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p",
                "isEmpty_p",
                "peek_obj_type_p", "push_p", "pop_p", "clear_p", "diff"]
        if fs12 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)

            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['isEmpty_p'] = df['isEmpty_p'].astype(str).str.lower()

            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['peek_obj_type_p'] = df['peek_obj_type_p'].astype(str).str.lower()

            data['push'] = df['push'].astype(str).str.lower()
            data['push_p'] = df['push_p'].astype(str).str.lower()

            data['pop'] = df['pop'].astype(str).str.lower()
            data['pop_p'] = df['pop_p'].astype(str).str.lower()

            data['clear'] = df['clear'].astype(str).str.lower()
            data['clear_p'] = df['clear_p'].astype(str).str.lower()

            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' or n == 'diff':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs13 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p",
                "isEmpty_p", "peek_obj_type_p", "push_p", "pop_p", "clear_p", 'calledMethod', "diff"]
        if fs13 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)

            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['isEmpty_p'] = df['isEmpty_p'].astype(str).str.lower()

            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['peek_obj_type_p'] = df['peek_obj_type_p'].astype(str).str.lower()

            data['push'] = df['push'].astype(str).str.lower()
            data['push_p'] = df['push_p'].astype(str).str.lower()

            data['pop'] = df['pop'].astype(str).str.lower()
            data['pop_p'] = df['pop_p'].astype(str).str.lower()

            data['clear'] = df['clear'].astype(str).str.lower()
            data['clear_p'] = df['clear_p'].astype(str).str.lower()

            data['calledMethod'] = df['calledMethod'].astype(str).str.lower()

            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' or n == 'diff':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

    else:

        fs6 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear"]
        if fs6 == columName:
            data['size'] = df['size'].astype(float)
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs7 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'size_p']
        if fs7 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs8 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", 'calledMethod',
               'size_p']
        if fs8 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['calledMethod'] = df['calledMethod'].astype(str).str.lower()
            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' :
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs12 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p",
                "isEmpty_p",
                "peek_obj_type_p", "push_p", "pop_p", "clear_p"]
        if fs12 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)

            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['isEmpty_p'] = df['isEmpty_p'].astype(str).str.lower()

            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['peek_obj_type_p'] = df['peek_obj_type_p'].astype(str).str.lower()

            data['push'] = df['push'].astype(str).str.lower()
            data['push_p'] = df['push_p'].astype(str).str.lower()

            data['pop'] = df['pop'].astype(str).str.lower()
            data['pop_p'] = df['pop_p'].astype(str).str.lower()

            data['clear'] = df['clear'].astype(str).str.lower()
            data['clear_p'] = df['clear_p'].astype(str).str.lower()

            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId' :
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

        fs13 = ["testId", "instanceId", "size", "isEmpty", "peek_obj_type", "push", "pop", "clear", "size_p",
                "isEmpty_p", "peek_obj_type_p", "push_p", "pop_p", "clear_p", 'calledMethod']
        if fs13 == columName:
            data['size'] = df['size'].astype(float)
            data['size_p'] = df['size_p'].astype(float)

            data['isEmpty'] = df['isEmpty'].astype(str).str.lower()
            data['isEmpty_p'] = df['isEmpty_p'].astype(str).str.lower()

            data['peek_obj_type'] = df['peek_obj_type'].astype(str).str.lower()
            data['peek_obj_type_p'] = df['peek_obj_type_p'].astype(str).str.lower()

            data['push'] = df['push'].astype(str).str.lower()
            data['push_p'] = df['push_p'].astype(str).str.lower()

            data['pop'] = df['pop'].astype(str).str.lower()
            data['pop_p'] = df['pop_p'].astype(str).str.lower()

            data['clear'] = df['clear'].astype(str).str.lower()
            data['clear_p'] = df['clear_p'].astype(str).str.lower()

            data['calledMethod'] = df['calledMethod'].astype(str).str.lower()

            transactions_df = data.copy()

            names = transactions_df.columns.values
            for n in names:
                if n == 'testId' or n == 'instanceId':
                    transactions_df[n] = df[n]
                else:
                    transactions_df[n] = str(n) + ' == ' + '"' + df[n].astype(str) + '"'

    return transactions_df


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-s', '-- One file or directory', 'direc', help=' *direc* for directory or *one* for one file')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, direc, file_out):
        print('*** Reading Data ***')
        paths = str(pathlib.Path().absolute()) + '\\' + 'EncodeDS'

        # if not os.path.exists(paths):
        #    os.mkdir('EncodeDS')

        if direc == 'directory':
            dataPath = gl.glob(file_in)
            for i in range(0, len(dataPath)):
                df = pd.read_csv(dataPath[i], index_col=0)
                name = dataPath[i].split('\\')
                name = name[-1]
                new_df = encoder(df)
                file_out_a = paths + '\\' + file_out
                name = file_out_a + name
                saveFile(new_df, name)

        else:
            df = pd.read_csv(file_in, index_col=0)
            new_df = encoder(df)
            saveFile(new_df, file_out)

main()
