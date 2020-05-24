import csv
with open('data/place_holder_suggest_question.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list_placeholder_message = []
    list_intent = []
    for row in csv_reader:
        list_placeholder_message.append(row[1])
        list_intent.append(row[0])