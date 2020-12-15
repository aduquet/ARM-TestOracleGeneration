call cd..

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod1_pop.csv -f CSV-labelling -o Mod3_clear_Mod1_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod2_pop.csv -f CSV-labelling -o Mod3_clear_Mod2_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod3_pop.csv-f CSV-labelling -o Mod3_clear_Mod3_pop

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod1_isEmpty.csv -f CSV-labelling -o Mod3_clear_Mod1_isEmpty
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod2_e.csv -f CSV-labelling -o Mod3_clear_Mod2_e

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod1_p.csv -f CSV-labelling -o Mod3_clear_Mod1_p
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod2_peek.csv -f CSV-labelling -o Mod3_clear_Mod2_peek
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod3_peek.csv -f CSV-labelling -o Mod3_clear_Mod3_peek

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod1_size.csv -f CSV-labelling -o Mod3_clear_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod2_size.csv -f CSV-labelling -o Mod3_clear_Mod2_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod3_size.csv -f CSV-labelling -o Mod3_clear_Mod3_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod3_clear/Mod3_clear_Mod3_s.csv -f CSV-labelling -o Mod3_clear_Mod3_s



