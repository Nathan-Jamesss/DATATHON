"""Remove the IoT/sensor tables from the shipped datasets and every mention of them in the problem statements."""
import os, re, json, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
DS = os.path.abspath('../site/datasets')

# 1) delete the IoT csvs
removed = []
for t in sorted(d for d in os.listdir(DS) if os.path.isdir(os.path.join(DS, d))):
    for f in os.listdir(os.path.join(DS, t)):
        if f.endswith('_iot.csv') or f == 'iot_vitals.csv':
            os.remove(os.path.join(DS, t, f)); removed.append(f)
print('removed:', removed)

# 2) READMEs
def sub(path, pairs):
    s = open(path, encoding='utf-8', newline='').read()
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8', newline='').write(s)

sub(f'{DS}/README.txt', [(' IoT tables are included in all four tracks to support optional sensor/edge/IoT work.', '')])
sub(f'{DS}/01_health_forgotten_patient/README.txt', [
    (', diagnostic_tests.csv (5,000), iot_vitals.csv (12,000).', ', diagnostic_tests.csv (5,000).'),
    ('diagnostic_tests.encounter_id and iot_vitals.encounter_id = encounters.encounter_id.', 'diagnostic_tests.encounter_id = encounters.encounter_id.')])
sub(f'{DS}/02_education_campus_space/README.txt', [
    ('class_schedule.csv (5,000), occupancy_iot.csv (25,000), room_requests.csv', 'class_schedule.csv (5,000), room_requests.csv'),
    ('rooms.room_id = class_schedule.room_id / occupancy_iot.room_id / events.room_id.', 'rooms.room_id = class_schedule.room_id / events.room_id.'),
    ('Use occupancy sensor fields as noisy signals; evaluate room matching, availability estimation, utilization and admin recommendations. Avoid assuming sensor readings always represent perfect occupancy.',
     'Evaluate room matching, availability estimation, utilization and admin recommendations.')])
sub(f'{DS}/03_smart_city_where_fix_first/README.txt', [
    ('incidents.csv (10,000), traffic_iot.csv (18,000), public_complaints.csv (8,000), environment_iot.csv (12,000).', 'incidents.csv (10,000), public_complaints.csv (8,000).'),
    ('location_id appears across all files.', 'location_id appears across all files.')])
sub(f'{DS}/04_business_money_leak/README.txt', [
    (', campaigns.csv (1,200), retail_iot.csv (10,000).', ', campaigns.csv (1,200).'),
    ('; campaign data can be analyzed by date/channel/category; retail_iot is at store level and may need aggregation to daily/time buckets.', '; campaign data can be analyzed by date/channel/category.')])

# 3) rebuild zips
tracks = sorted(d for d in os.listdir(DS) if os.path.isdir(os.path.join(DS, d)))
stats = {}
for t in tracks:
    files = sorted(os.listdir(os.path.join(DS, t)))
    with zipfile.ZipFile(os.path.join(DS, t + '.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files: z.write(os.path.join(DS, t, f), t + '/' + f)
    stats[t] = {}
    for f in files:
        if f.endswith('.csv'):
            p = os.path.join(DS, t, f)
            with open(p, 'rb') as fh: rows = sum(1 for _ in fh) - 1
            stats[t][f] = [rows, os.path.getsize(p)]
with zipfile.ZipFile(os.path.join(DS, 'DATATHON_All_Track_Datasets.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(DS, 'README.txt'), 'datathon_datasets/README.txt')
    for t in tracks:
        for f in sorted(os.listdir(os.path.join(DS, t))): z.write(os.path.join(DS, t, f), f'datathon_datasets/{t}/{f}')
json.dump(stats, open('stats.json', 'w'))
print({t: len(v) for t, v in stats.items()})

# 4) problem-statement text
b = open('build.py', encoding='utf-8').read()
b = re.sub(r', \("[a-z_]*iot\.csv", "[^"]*"\)', '', b)
for a, c in [
    ('"A room-availability estimate using schedule and occupancy signals."', '"A room-availability estimate using the class schedule and room requests."'),
    ('occupancy signals approximate actual use; ', ''),
    ('identify schedule/occupancy mismatches, ', ''),
    ('Occupancy estimation, availability classification', 'Availability classification'),
    ('"A sensor anomaly or traffic-congestion alert.", ', ''),
    ('road conditions, traffic, and sensor readings to be brought together', 'road conditions and context to be brought together'),
    ('; the retail activity table adds store activity and checkout queue signals.', '.'),
    ('The device-vitals table is simulated and is <b>not</b> suitable for clinical diagnosis.', 'This data is simulated and is <b>not</b> suitable for clinical diagnosis.'),
]:
    if a not in b: print('NOT FOUND:', a[:60])
    b = b.replace(a, c)
open('build.py', 'w', encoding='utf-8').write(b)
print('ok')
