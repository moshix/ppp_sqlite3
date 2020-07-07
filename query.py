mport sqlite3
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
# copyright 2020 by moshix
# Apache 2.0 license
businessr   = sys.argv[1]
business    = businessr.encode('utf-8', 'ignore').decode('utf-8')
db     = sqlite3.connect("ppp.db")
cursor = db.cursor()
cursor.execute( "SELECT distinct BusinessName, State, City, Zip, LoanRange, Lender from ppp WHERE BusinessName like '%{bu}%' ORDER BY businessname ASC LIMIT 35".format(bu=business))
rows   = cursor.fetchall()
for row in rows:
#    print row
    print 'BUSINESS                       STATE  CITY           ZIP         LOANRANGE             LENDER'
    print '-------------------------------------------------------------------------------------------------------------------------------'
    print '\n%s     %s     %s        %s       %s   %s' % (row[0], row[1], row[2], row[3], row[4], row[5])
    print '      '
    print '      '
    print '      '
if len(rows)==0:
   print('RELAY999I: No results found in database ')
   print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ')
