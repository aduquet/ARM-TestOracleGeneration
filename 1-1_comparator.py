import os
import pathlib
import warnings
import pandas as pd
import datetime

warnings.filterwarnings('ignore')


def insert_row(idx, df, df_inset, k):

    for i in range(0, k):
        df = df.iloc[:idx, ].append(df_inset).append(df.iloc[idx:, ]).reset_index(drop=True)
        idx = idx + 1
        # print(idx)

    return df


def comp(no_modi_df, modi_df, modiLabel_df):
    no_modi_df.drop(columns=['testId', 'instanceId'], inplace=True)
    modi_df.drop(columns=['testId', 'instanceId'], inplace=True)
    modiLabel_df['diff'] = 'No'

    df = no_modi_df.eq(modi_df)
    for index, row in df.iterrows():
        if not row['peek_obj_type']:
            modiLabel_df['diff'][index] = 'Yes'

        if not row['isEmpty']:
            modiLabel_df['diff'][index] = 'Yes'

        if not row['size']:
            modiLabel_df['diff'][index] = 'Yes'

        if not row['calledMethod']:
            modiLabel_df['diff'][index] = 'Yes'

        if not row['pushInput']:
            modiLabel_df['diff'][index] = 'Yes'

    return modiLabel_df


def comp2(no_modi_df, modi_df, modiAux_df):
    j = 0
    for index, row in no_modi_df.iterrows():
        no_df = no_modi_df.copy()
        df = modi_df.copy()

        testID_noDF = no_df.at[j, 'testId']
        testID_DF = df.at[j, 'testId']
        # print('este testID', testID_DF)
        # print('este testID2', testID_noDF)
        no_df.drop(no_df[no_df['testId'] != testID_noDF].index, inplace=True)
        df.drop(df[df['testId'] != testID_DF].index, inplace=True)
        if len(no_df) != len(df):
            dif = abs(len(no_df) - len(df))
        #    print('este es', dif)
        #    print('este es', j)
            modi_df = insert_row(j+len(df), modi_df, modiAux_df, k=dif)
            # modi_df.to_csv('test.csv')
            #   print(modi_df)
            j = j + len(no_df)
        else:
            j = j + len(df)
        if len(modi_df) == len(no_modi_df):
            return modi_df
        # print(j)


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--first file', 'file_in', help='Path for getting the data')
    @click.option('-m', '--second file', 'file_in2', help='Path for getting the data')
    @click.option('-f', '-- file', 'file', help='Name of the directory in which data will be stored')
    @click.option('-o', '--out file', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, file_in2, file, file_out):
        begin_time = datetime.datetime.now()
        No_modi = pd.read_csv(file_in, index_col=None)
        modi = pd.read_csv(file_in2, index_col=None)

        modiLabel = modi.copy()
        print('*** Reading Data ***')

        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        if len(No_modi) == len(modi):
            modiLabel = comp(No_modi, modi, modiLabel)
            name = file_out + '.csv'
            file_out_aux = paths + '\\'
            modiLabel.to_csv(file_out_aux + name, index=False)
            t = open(file_out + "_timeReport.txt", 'w')
            t.write(str(datetime.datetime.now() - begin_time))
            t.close()

        else:
            newRow = [('--', '--', '--', '--', '--', '--', '--', '--')]
            dfAux = pd.DataFrame(newRow, columns=No_modi.columns, index=None)
            modiLabelAux = comp2(No_modi, modi, dfAux)
            modiLabelAux2 = modiLabelAux.copy()
            finalDF = comp(No_modi, modiLabelAux, modiLabelAux2)
            name = file_out + '.csv'
            file_out_aux = paths + '\\'
            finalDF.to_csv(file_out_aux + name, index=False)
            t = open(file_out + "_timeReport.txt", 'w')
            t.write(str(datetime.datetime.now() - begin_time))
            t.close()
            print('done!')

main()
