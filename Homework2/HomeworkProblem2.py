# Mohammad Qureshi
# PSID 1789301
# Homework Problem 2

# CURRENT DATE
import datetime
current_time = datetime.datetime.now()
current_year = current_time.year
current_month = current_time.month
current_day = current_time.day


# LIST OF ALL THE MONTHS
month_list = ['January','February','March','April','May','June', 'July','August','September','October','November','December']


# PART A
# TAKES USER INPUT OF DATES
# IF USER INPUT IS CORRECT, OUTPUTS NEW DATE FORMAT
# LOOP UNTIL -1 IS INPUT
date = 1
while date != -1:
  date = input("Enter the month day, year: ")
  if date =='-1':
    break
  else:
    if date != '-1':
      my_list = date.split()
      if len(my_list) != 3:
        continue
      month = my_list[0]
      day = my_list[1]
      year = my_list[2]
      new_day = day.replace(',','')

      for m in range(12):
          if date.find(month_list[m])>=0:
            month_num = m+1
            final_date = ('{}/{}/{}'.format(month_num, new_day, year))
            print(final_date)
            break
      continue

# PART B
# OPENS inputDates FILE AMD READS CONTENT
date_b = open('inputDates.txt', 'r')
file_contents = date_b.read()
print(file_contents)
date_b.close()

# PART C
# OPENS inputDates FILE AND TRANSFERS CORRECT INFORMATION TO parsedDates FILE
with open('inputDates.txt','r') as input_c:
    date_c = input_c.readlines()

    counter = 0
    for part in date_c:
      counter = counter + 1
      if part =='-1':
        break

      if part != '-1':
        list = part.split()
        if len(list) != 3:
          continue
        month_c = list[0]
        day_c = list[1]
        year_c = list[2]
        new_day_c = day_c.replace(',', '')

        for m in range(12):
          if part.find(month_list[m])>=0:
            m_c = str(m+1)
            if int(year_c) > current_year:
              continue
            else:
              final_ouput = m_c + '/' + new_day_c + '/' + year_c

            i = 0
            if counter > i:
              output_c = open('parsedDates.txt','a')
              output_c.write(final_ouput + '\n')
              output_c.close()
            else:
              break
        continue

    input_c.close()