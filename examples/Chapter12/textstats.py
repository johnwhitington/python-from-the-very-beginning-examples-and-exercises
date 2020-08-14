import sys
import textstat

if len(sys.argv) > 1:
    ls, cs, ws, ss = textstat.stats_from_filename(sys.argv[1])
    print(f'{ls} lines, {cs} characters, {ws} words, {ss} sentences')
    
