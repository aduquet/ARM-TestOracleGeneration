call cd..

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod1_p.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod1_p
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod2_peek.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod2_peek
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod3_peek.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod3_peek

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod1_pop.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod1_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod2_pop.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod2_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod3_pop.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod3_pop

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod1_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod2_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod2_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod3_size.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod3_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-threeFaults-Mod1_isEmpty_Mod2_clear/Mod1_isEmpty_Mod2_clear_Mod3_s.csv -f CSV-labelling -o Mod1_isEmpty_Mod2_clear_Mod3_s





