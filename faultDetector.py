import warnings

warnings.filterwarnings('ignore')
import os
import pandas as pd
import numpy as np
from collections import defaultdict


def preProsDF(df):
    df = df.drop(df[df['Violated'] == 0].index)
    df = df.drop_duplicates(subset=['Violated'], keep='last')
    return df


def takeViolations(set_rule):
    # print(type(setRule))
    set_rule = set_rule.replace(' ', '')
    set_rule = set_rule.replace("'", '')
    set_rule = set_rule.replace(']', '')
    set_rule = set_rule.replace('[', '')
    set_rule = set_rule.split(',')

    return set_rule


def preProsRules(set_rule, dfr):
    set_rule = [int(x) for x in set_rule]
    Filter_dfr = dfr[dfr.index.isin(set_rule)]
    return Filter_dfr
    # RHS[]


def counterItem(item, rows, fin, WHS):
    # print('counter item')
    # print(item)
    # print(rows)
    # print(fin)
    # print(WHS)
    times = 0
    if WHS == 'RHS':
        for i in rows:
            # print('*****', i)
            # print('ROW', item)
            if i.find(item) != -1:
                times += 1
                #    print(times)
                mainDictRHS[item] = times
            #else:
             #   mainDictRHS[item] = 20
        # print(mainDictRHS)
        if fin == 6:
            # print(mainDictRHS)
            return mainDictRHS

    if WHS == 'LHS':
        for i in rows:
            if i.find(item) != -1:
                times += 1
                mainDictLHS[item] = times
            #else:
             #   mainDictLHS[item] = 1000

        if fin == 6:
            return mainDictLHS


def counter(set_rule):
    # print(set_rule)
    items = list(mainDictLHS.keys())
    RHS = set_rule['RHS']
    LHS = set_rule['LHS']
    rhs_aux = []
    lhs_aux = []

    for row in RHS:
        # print('****',row)
        if row.find(',)') == -1:
            rhs = row.replace(' ', '')
            rhs = rhs.replace("'", '')
            # print(rhs)
            rhs = rhs.replace('(', '')
            rhs = rhs.replace(')', '')
            rhs = rhs.split(',')
            rhs_aux.extend(rhs)
        else:
            rhs_1 = row.replace('(', '')
            rhs_1 = rhs_1.replace("'", '')
            rhs_1 = rhs_1.replace(',', '')
            rhs_1 = rhs_1.replace(')', '')
            rhs_aux.append(rhs_1)

    for row in LHS:
        # print('****',row)
        if row.find(',)') == -1:
            lhs = row.replace(' ', '')
            lhs = lhs.replace("'", '')
            # print(rhs)
            lhs = lhs.replace('(', '')
            lhs = lhs.replace(')', '')
            lhs = lhs.split(',')
            lhs_aux.extend(lhs)
        else:
            lhs_1 = row.replace('(', '')
            lhs_1 = lhs_1.replace("'", '')
            lhs_1 = lhs_1.replace(',', '')
            lhs_1 = lhs_1.replace(')', '')
            lhs_aux.append(lhs_1)
    fin = 0

    for i in items:
        fin += 1
        #   print(fin)
        t = counterItem(i, rhs_aux, fin, 'RHS')
        tl = counterItem(i, lhs_aux, fin, 'LHS')
    # print('RHS', t)
    # print('LHS', tl)

    return tl, t, len(RHS)


def lhs_rhs(df, file_out):
    # print(df.keys())
    # df['lhs_rhs-peek_obj_type'] = df['LHS_peek_obj_type'] / df['RHS_peek_obj_type']
    # df['lhs_rhs-isEmpty'] = df['LHS_isEmpty'] / df['RHS_isEmpty']
    # df['lhs_rhs-size'] = df['LHS_size'] / df['RHS_size']
    # df['lhs_rhs-push'] = df['LHS_push'] / df['RHS_push']
    # df['lhs_rhs-pop'] = df['LHS_pop'] / df['RHS_pop']
    # df['lhs_rhs-clear'] = df['LHS_clear'] / df['RHS_clear']
    # df['lhs_rhs-peek_obj_typ_p'] = df['LHS_peek_obj_type_p'] / df['RHS_peek_obj_type_p']
    # df['lhs_rhs-isEmpty_p'] = df['LHS_isEmpty_p'] / df['RHS_isEmpty_p']
    # df['lhs_rhs-size_p'] = df['LHS_size_p'] / df['RHS_size_p']
    # df['lhs_rhs-push_p'] = df['LHS_push_p'] / df['RHS_push_p']
    # df['lhs_rhs-pop_p'] = df['LHS_pop_p'] / df['RHS_pop_p']
    # df['lhs_rhs-clear_p'] = df['LHS_clear_p'] / df['RHS_clear_p']
    #df.replace(50, 'No item', inplace=True)
    #df.replace(1000, 'No item', inplace=True)
    #df.replace(20, 'No item', inplace=True)

    df.to_csv(file_out)
    print('Done')


if __name__ == '__main__':
    import click

    global mainDictRHS
    # mainDictRHS = defaultdict()
    mainDictRHS = {'peek_obj_type': 0, 'isEmpty': 0, 'size': 0, 'push': 0, 'pop': 0, 'clear': 0}
    # 'peek_obj_type_p': 0, 'isEmpty_p': 0, 'size_p': 0, 'push_p': 0, 'pop_p': 0, 'clear_p': 0}

    global itemCount
    itemCount = {}

    global mainDictLHS
    mainDictLHS = {'peek_obj_type': 0, 'isEmpty': 0, 'size': 0, 'push': 0, 'pop': 0, 'clear': 0}


    # ,'peek_obj_type_p': 0, 'isEmpty_p': 0, 'size_p': 0, 'push_p': 0, 'pop_p': 0, 'clear_p': 0}

    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-r', '--rules', 'rules', help='set of rules')
    @click.option('-o', '--out file', 'file_out', help='output name')
    def main(file_in, rules, file_out):
        item_count = pd.DataFrame()
        col = list(mainDictRHS.keys())
        # print('*** Reading Data ***')
        df = pd.read_csv(file_in, index_col=0)
        dfr = pd.read_csv(rules, index_col=0)
        # print(dfr.head(10))
        df = preProsDF(df)
        # print(df.head(10))
        df = df.reset_index()
        rulesV = df['RuleViolated']
        aux = []
        flag = 0
        if rulesV.empty:
            a = 0
            # print(rulesV)

        else:
            for row in rulesV:
                setRule = takeViolations(row)
                set_ruleF = preProsRules(setRule, dfr)
                set_ruleF = set_ruleF[['LHS', 'RHS']]
                lhs, rhs, tam = counter(set_ruleF)
                # print(lhs)
                # print(rhs)
                if lhs is None:
                    pass
                #    print('adsfa', lhs)
                # flag = 0
                else:
                    #    print(lhs)
                    item_count = {'Number_of_Rules': tam, 'LHS_peek_obj_type': lhs['peek_obj_type'],
                                  'LHS_isEmpty': lhs['isEmpty'], 'LHS_size': lhs['size'], 'LHS_push': lhs['push'],
                                  'LHS_pop': lhs['pop'], 'LHS_clear': lhs['clear'],
                                  'RHS_peek_obj_type': rhs['peek_obj_type'], 'RHS_isEmpty': rhs['isEmpty'],
                                  'RHS_size': rhs['size'], 'RHS_push': rhs['push'], 'RHS_pop': rhs['pop'],
                                  'RHS_clear': rhs['clear']}
                    # item_count = {'Number_of_Rules': tam, 'LHS_peek_obj_type': lhs['peek_obj_type'], 'LHS_isEmpty':
                    # lhs['isEmpty'], 'LHS_size': lhs['size'], 'LHS_push': lhs['push'], 'LHS_pop': lhs['pop'],
                    # 'LHS_clear': lhs['clear'], 'LHS_peek_obj_type_p': lhs['peek_obj_type_p'], 'LHS_isEmpty_p': lhs[
                    # 'isEmpty_p'], 'LHS_size_p': lhs['size_p'], 'LHS_push_p': lhs['push_p'], 'LHS_pop_p': lhs['pop_p'],
                    # 'LHS_clear_p': lhs['clear_p'], 'RHS_peek_obj_type': rhs['peek_obj_type'], 'RHS_isEmpty': rhs[
                    # 'isEmpty'], 'RHS_size': rhs['size'], 'RHS_push': rhs['push'], 'RHS_pop': rhs['pop'],
                    # 'RHS_clear':rhs['clear'], 'RHS_peek_p': rhs['peek_obj_type_p'], 'RHS_isEmpty_p': rhs['isEmpty_p'],
                    # 'RHS_size_p': rhs['size_p'],  'RHS_push_p': rhs['push_p'], 'RHS_pop_p': rhs['pop_p'],
                    # 'RHS_clear_p':rhs['clear_p']}
                    #
                    aux.append(item_count)
                    # print(aux)
                    flag = 1

            if flag == 1:
                final = pd.DataFrame(aux)
                # print(final)
                lhs_rhs(final, file_out)
main()
