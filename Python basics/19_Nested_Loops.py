
# todo: single loop:
print('single loop!')
for i in range(1, 6):
    print(i)
else:
    print("Hole loop itreat")

# todo: Double loop:
print('double nested loop!')
for x in range(3):
    for y in range(2):
        print(f'{x}:{y}')
else:
    print("Hole loop itreat")

# todo: Triple loop:
print('triple nested loop!')
for x in range(3):
    for y in range(2):
        for z in range(1):
            print(f'{x}:{y}:{z}')
else:
    print("Hole loop itreat")

# todo: Genrate report_year_month_day.csv files:
print("create report.csv files!")
years = [2025, 2026]
months = ['nov', 'dec']
days = range(1, 10)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')
else:
    print("Hole loop itreat")


# todo: Genrate SQL:
# todo: SELECT count(*) FROM customers where id IS NULL;
tables = ['customers', 'orders', 'products', 'prices']
colums = ['id', 'create_date']
for t in tables:
    for c in colums:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')
