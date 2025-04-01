-- Average trip distance per vehicle
SELECT vehicle_id, AVG(distance_km) AS avg_distance
FROM trips
GROUP BY vehicle_id;

-- Utilization: Trips per day
SELECT DATE(trip_start_time) AS trip_date, COUNT(*) AS trip_count
FROM trips
GROUP BY trip_date;

-- Maintenance frequency
SELECT vehicle_id, COUNT(*) AS maintenance_events
FROM maintenance_logs
GROUP BY vehicle_id;
