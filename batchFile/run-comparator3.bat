call cd..

call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod1_clear.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod1_clear
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod2_clear.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod2_clear
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod3_clear.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod3_clear

call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod1_isEmpty.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod1_isEmpty
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod2_e.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod2_e

call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod1_p.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod1_p
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod2_peek.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod2_peek
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod3_peek.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod3_peek

call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod1_size.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod1_size
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod2_size.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod2_size
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod3_size.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod3_size
call python 1-1_comparator.py -i Not_Modified.csv -m CSV-threeFaults-Mod3_push_Mod3_pop/Mod3_push_Mod3_pop_Mod3_s.csv -f CSV-labelling -o Mod3_push_Mod3_pop_Mod3_s
