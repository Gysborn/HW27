import csv
import json


def csv_to_json(f_csv, f_json, model):
    result = []
    with open(f_csv, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for row in rows:
            del row['id']
            if model == 'ads.ad':
                row['price'] = int(row['price'])
                if row['is_published'] == "TRUE":
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            record = {'model': model, 'fields': row}
            result.append(record)

    with open(f_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)


csv_to_json('ads.csv', 'ads.json', 'ads.ad')
csv_to_json('category.csv', 'category.json', 'ads.categories')
csv_to_json('user.csv', 'user.json', 'users.user')
csv_to_json('location.csv', 'location.json', 'users.location')

