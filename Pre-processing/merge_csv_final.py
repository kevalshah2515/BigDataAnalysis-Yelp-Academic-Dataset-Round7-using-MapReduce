import csv
inputs = ["newreview.csv", "newbusiness.csv", "userlatest.csv"]  # etc

# First determine the field names from the top line of each input file
# Comment 1 below
fieldnames = [ 'type', 'latitude', 'business_id', 'categories', 'is_open', 'neighborhood', 'review_count', 'state', 'city', 'stars', 'longitude', 'funny', 'user_id', 'review_id', 'date', 'useful', 'cool', 'average_stars', 'name', 'address']
for filename in inputs:
  with open(filename, "r", newline="" ,encoding="utf8") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        fieldnames.append(h)
print(fieldnames)       
#fieldnames = ["CCC","DDD","EEE","FFF"]

#count = 0


# Then copy the data
with open("out-put.csv", "w", newline="", encoding="utf8") as f_out:   # Comment 2 below
  writer = csv.DictWriter(f_out, fieldnames=fieldnames)

  abc = csv.writer(f_out)
  #for val in fieldnames:
  #      abc.writerow([val])

  abc.writerow(fieldnames)
  
  for filename in inputs:
    with open(filename, "r", newline="", encoding="utf8") as f_in:
      reader = csv.DictReader(f_in)  # Uses the field names in this file
      
      for line in reader:
        # Comment 3 below
        writer.writerow(line)
