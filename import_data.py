cat > import_data.py << 'EOF'
import csv
from cassandra.cluster import Cluster

CSV_PATH = '/train.csv'

def to_int(v):
    try:
        return int(v)
    except:
        return None

cluster = Cluster(['elassandra'])
session = cluster.connect('socialks')

insert_q = session.prepare("""
INSERT INTO social_media_usage (
    user_id, age, gender, platform,
    daily_usage_time_minutes,
    posts_per_day, likes_received_per_day,
    comments_received_per_day,
    messages_sent_per_day,
    dominant_emotion
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""")

with open(CSV_PATH, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        session.execute(insert_q, (
            row['User_ID'],
            to_int(row['Age']),
            row['Gender'],
            row['Platform'],
            to_int(row['Daily_Usage_Time (minutes)']),
            to_int(row['Posts_Per_Day']),
            to_int(row['Likes_Received_Per_Day']),
            to_int(row['Comments_Received_Per_Day']),
            to_int(row['Messages_Sent_Per_Day']),
            row['Dominant_Emotion'],
        ))
        count += 1

print(f"Importación completa → {count} filas insertadas 🎉")
EOF
