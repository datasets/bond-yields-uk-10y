# http://www.bankofengland.co.uk/boeapps/iadb/help.asp#CSV
# TT = tabular with titles, TN = tabular no titles. We do not want titles.
curl "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUAAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963&Dateto=01/Jan/2015" > cache/10y.csv
curl "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUMAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963&Dateto=01/Jan/2015" > cache/10y-m.csv
curl "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUQAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963&Dateto=01/Jan/2015" > cache/10y-q.csv
curl "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUAAAJLW&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963&Dateto=01/Jan/2015" > cache/10y-real.csv

