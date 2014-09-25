import MySQLdb,csv,time,datetime,winsound

now = time.time()

#Connect to database
myDB = MySQLdb.connect(host="zzz.yyy.net", port=3306, db="ddd")

#Get cursor object
cHandler = myDB.cursor()

#Send select request for specific entries
sqlCommand = "SELECT STR_TO_DATE(date,'%m/%d/%Y'), count(*) \
              FROM some_db_table \
              WHERE STR_TO_DATE(date,'%m/%d/%Y') between '2013-10-12' AND '2013-10-20' \
              GROUP BY STR_TO_DATE(date,'%m/%d/%Y') \
              order by 1 desc"
cHandler.execute(sqlCommand)

#View results
results = cHandler.fetchall()

#write results to file
with open('Results.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['Date','# Records'])
    writer.writerows(results)

print ''
'''
print '~' * 30
print ' Query complete'
print '~' * 30
'''
print 'Date','\t\t','# of Records'
print '----------','\t','------------'
for row in results:
    print row[0],'\t',row[1]

print ''
print "Number of rows returned: %d" % cHandler.rowcount
print ''
print "It took %0.02d secs to run this program" % (time.time() - now)
print ''
#print 'Current time is %s' % datetime.datetime.now().time()
#print ''
t=time.localtime()
print 'Date:',time.strftime("%a, %d %b %Y",t)
print 'Time:',time.strftime("%H:%M:%S",t)

#plot results
dates = []
records = []
for row in results:
    dates.append(row[0])
    records.append(row[1])
plt.plot(dates, records)
plt.title('Results of Query')
plt.show()

myDB.close()

#print Play an evil laugh when complete
winsound.PlaySound('evil_laugh.wav',winsound.SND_FILENAME)

