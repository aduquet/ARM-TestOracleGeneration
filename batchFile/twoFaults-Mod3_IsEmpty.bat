call cd..

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_clear.csv -f CSV-labelling -o Mod1_isEmpty_Mod1_clear
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod2_clear.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_peek.csv -f CSV-labelling -o Mod1_isEmpty_Mod1_peek
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod3_peek.csv -f CSV-labelling -o Mod1_isEmpty_Mod3_peek

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_pop.csv -f CSV-labelling -o Mod1_isEmpty_Mod1_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod2_pop.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_pop

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_push.csv -f CSV-labelling -o Mod1_isEmpty_Mod1_push
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod2_push.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_push

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-Stack/CSV-twoFaults-Mod1_isEmpty/Mod1_isEmpty_Mod1_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod3_size



