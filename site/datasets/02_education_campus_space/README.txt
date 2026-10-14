EDUCATION — THE CAMPUS HAS SPACE. STUDENTS DON'T.
Synthetic educational dataset created for DATATHON. It is not a live campus booking system.
Files: rooms.csv (120), class_schedule.csv (5,000), occupancy_iot.csv (25,000), room_requests.csv (5,000), events.csv (1,800).
Join keys: rooms.room_id = class_schedule.room_id / occupancy_iot.room_id / events.room_id. There is no guaranteed room_id on requests because requests represent demand before allocation.
Use occupancy sensor fields as noisy signals; evaluate room matching, availability estimation, utilization and admin recommendations. Avoid assuming sensor readings always represent perfect occupancy.
