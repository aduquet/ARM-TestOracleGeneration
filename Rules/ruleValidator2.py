import pandas as pd
import os
import pathlib
import warnings
import datetime
import glob as gl

warnings.filterwarnings('ignore')


def saveReport(name, df, file_out, file, p):
    df.to_csv(file + '\\' + file_out + name)
    t = open(file_out+ "_timeReport.txt", 'w')
    t.write(str(datetime.datetime.now() - p))
    t.close()
    #print('done!')


def matchLHS(data, dfReport, sizeLHS, lhsAux, sizeRHS, rhsAux, k, file_out, file, ti):
    for index, row in data.iterrows():
        listData = list(row)
        count = 0
        # print('REGLAS', lhsAux, rhsAux)
        # print('FILA', listData, '\n')
        for i in lhsAux:
            if i in listData:
                count = count + 1
                # print(i)
                if count == sizeLHS:
                    if matchRHS(listData, sizeRHS, rhsAux):
                        counter = dfReport['Matched'].values[index]
                        rax = list(dfReport['RuleMatched'].values[index])
                        rax.append(str(k))
                        dfReport.at[index, 'Matched'] = counter + 1
                        dfReport.at[index, 'RuleMatched'] = rax
                        saveReport('ruleValidator.csv', dfReport, file_out, file, ti)
                    else:
                        counter = dfReport['Violated'].values[index]
                        rax = list(dfReport['RuleViolated'].values[index])
                        rax.append(str(k))
                        dfReport.at[index, 'Violated'] = counter + 1
                        dfReport.at[index, 'RuleViolated'] = rax

                        counter = dfReport['Matched_LHS'].values[index]
                        rax = list(dfReport['RuleMatched_LHS'].values[index])
                        rax.append(str(k))
                        dfReport.at[index, 'Matched_LHS'] = counter + 1
                        dfReport.at[index, 'RuleMatched_LHS'] = rax

                        saveReport('ruleValidator.csv', dfReport, file_out, file , p= ti)
                # matchRHSsaver(listData, sizeRHS, rhsAux, dfReport, index, k, file_out)
            else:
                # matchRHSsaver(listData, sizeRHS, rhsAux, dfReport, index, k, file_out)
                break


def matchRHS(listData, sizeRHS, rhsAux):
    count = 0
    for i in rhsAux:
        if i in listData:
            count = count + 1
            # print(i)
            if count == sizeRHS:
                return True
        else:
            break


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-r', '--file rules', 'file_rules', help='Path for getting the rules')
    @click.option('-f', '--file', 'file', help='Name of the directory in which data will be store')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')
    def main(file_in, file_rules, file_out, file):
        begin_time = datetime.datetime.now()
        paths = str(pathlib.Path().absolute()) + '\\' + file

        if not os.path.exists(paths):
            os.mkdir(file)

        dataPath = gl.glob(file_in)

        for i in range(0, len(dataPath)):
            df = pd.read_csv(dataPath[i])

            df_rules = pd.read_csv(file_rules)
            data = pd.read_csv(file_in)
            dfReport = data.copy()

            dfReport['Matched_LHS'] = 0
            dfReport['RuleMatched_LHS'] = ''

            # dfReport['Matched_RHS'] = 0
            # dfReport['RuleMatched_RHS'] = ''

            dfReport['Matched'] = 0
            dfReport['RuleMatched'] = ''

            dfReport['Violated'] = 0
            dfReport['RuleViolated'] = ''
            # df_rules = df_rules.head(100)

            for index, row in df_rules.iterrows():
                lhsAux = []
                rhsAux = []
                if df_rules['LHS_size'].at[index] >= 1:
                    rAux = df_rules['LHS'].at[index]
                    sizeLHS = df_rules['LHS_size'].at[index]
                    # print(rAux)
                    rAux = list(rAux)
                    rAux.remove('(')
                    rAux.remove(')')
                    # rAux.remove(' ')
                    b = "".join(rAux)
                    lhs = b.split(',')
                    # print('LHS:', lhs)

                    for i in lhs:
                        b = i.replace("'", "")
                        b = b.lstrip()
                        lhsAux.append(b)
                    # print(lhsAux)

                    rAux = df_rules['RHS'].at[index]
                    sizeRHS = df_rules['RHS_size'].at[index]
                    # print(rAux)
                    rAux = list(rAux)
                    rAux.remove('(')
                    rAux.remove(')')
                    # rAux.remove(' ')
                    b = "".join(rAux)
                    rhs = b.split(',')
                # print('RHS:', rhs)

                for i in rhs:
                    b = i.replace("'", "")
                    b = b.lstrip()
                    rhsAux.append(b)
                # print(rhsAux)

                # data = data.head(5)
                #
                # print(index)
                matchLHS(data, dfReport, sizeLHS, lhsAux, sizeRHS, rhsAux, index, file_out, file, begin_time)
                # if MatchLHS:
                #     MatchRHS = matchRHS(data, sizeRHS, rhsAux)
                # match(data, lhsAux, sizeLHS, rhsAux, sizeRHS, dfReport, index, file_out)

        print('\n *** Report Saved ***')

main()