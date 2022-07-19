import gspread

gc = gspread.service_account(filename='hu.json')
sh = gc.open('hurawatch').sheet1

sh.append_row(['Title','Year', 'Duration',"Link"])