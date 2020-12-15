call cd..
call python newUniqueRows.py -i CSV-NoModified/* -s dire -f nur_ -o nur_noMod

call python newUniqueRows.py -i EncodeDS/FS6/A/* -s dire -f unr-FS6 -o unr_AFS6_
call python newUniqueRows.py -i EncodeDS/FS7/A/* -s dire -f unr-FS7 -o unr_AFS7_
call python newUniqueRows.py -i EncodeDS/FS8/A/* -s dire -f unr-FS8 -o unr_AFS8_
call python newUniqueRows.py -i EncodeDS/FS12/A/* -s dire -f unr-FS12 -o unr_AFS12_
call python newUniqueRows.py -i EncodeDS/FS13/A/* -s dire -f unr-FS13 -o unr_AFS13_

call python newUniqueRows.py -i EncodeDS/FS6/B/* -s dire -f unr-FS6 -o unr_BFS6_
call python newUniqueRows.py -i EncodeDS/FS7/B/* -s dire -f unr-FS7 -o unr_BFS7_
call python newUniqueRows.py -i EncodeDS/FS8/B/* -s dire -f unr-FS8 -o unr_BFS8_
call python newUniqueRows.py -i EncodeDS/FS12/B/* -s dire -f unr-FS12 -o unr_BFS12_
call python newUniqueRows.py -i EncodeDS/FS13/B/* -s dire -f unr-FS13 -o unr_BFS13_