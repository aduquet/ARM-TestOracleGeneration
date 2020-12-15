call cd..
call python featureSelector.py -i CSV-labelling\twoFaults-Mod1_isEmpty/* -s dir -f historicalData -o h_
call python historyCreator.py -i CSV-labelling/twoFaults-Mod2_peek/* -s dir -f historicalData -o h_
call python historyCreator.py -i CSV-labelling/twoFaults-Mod2_size/* -s dir -f historicalData -o h_
call python historyCreator.py -i CSV-labelling/twoFaults-Mod3_clear/* -s dir -f historicalData -o h_
call python historyCreator.py -i CSV-labelling/twoFaults-Mod3_pop/* -s dir -f historicalData -o h_
call python historyCreator.py -i CSV-labelling/twoFaults-Mod3_push/* -s dir -f historicalData -o h_