call cd..

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod1_push.csv -f CSV-labelling -o Mod2_peek_Mod1_push
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod2_push.csv -f CSV-labelling -o Mod2_peek_Mod2_push

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod1_pop.csv -f CSV-labelling -o Mod2_peek_Mod1_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod2_pop.csv -f CSV-labelling -o Mod2_peek_Mod2_pop

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod1_clear.csv -f CSV-labelling -o Mod2_peek_Mod2_clear
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod2_clear.csv -f CSV-labelling -o Mod2_peek_Mod2_clear

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod2_isEmpty.csv-f CSV-labelling -o Mod2_peek_Mod2_isEmpty
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod3_isEmpty.csv-f CSV-labelling -o Mod2_peek_Mod3_isEmpty

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod1_size.csv -f CSV-labelling -o Mod2_peek_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod2_size.csv -f CSV-labelling -o Mod2_peek_Mod2_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod2_peek/Mod2_peek_Mod3_size.csv -f CSV-labelling -o Mod2_peek_Mod3_size




