call cd..

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod1_pop.csv -f CSV-labelling -o Mod1_p_Mod1_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod2_pop.csv -f CSV-labelling -o Mod1_p_Mod2_pop
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod3_pop.csv -f CSV-labelling -o Mod1_p_Mod3_pop

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod1_isEmpty.csv -f CSV-labelling -o Mod1_p_Mod1_isEmpty

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod1_size.csv -f CSV-labelling -o Mod1_p_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod2_size.csv -f CSV-labelling -o Mod2_p_Mod1_size
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod3_size.csv -f CSV-labelling -o Mod3_p_Mod1_size

call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod1_clear.csv -f CSV-labelling -o Mod1_p_Mod1_clear
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod2_clear.csv -f CSV-labelling -o Mod1_p_Mod2_clear
call python 1-1_comparator.py -i CSV-Stack/Not_Modified.csv -m CSV-twoFaults-Mod1_p/Mod1_p_Mod3_clear.csv -f CSV-labelling -o Mod1_p_Mod3_clear



