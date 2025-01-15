SELECT parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address
FROM wap_devices
LIMIT 100;

SELECT *
FROM wap_devices
LIMIT 100;

SELECT parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address
FROM wap_devices
WHERE mac_vendor = 'Camera';

SELECT parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address
FROM wap_devices
WHERE parent_ipv4_address = '10.142.63.195';

SELECT parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address
FROM wap_devices
WHERE mac_vendor like 'XBOX';

SELECT COUNT(*)
FROM wap_devices
WHERE mac_vendor like '%XBOX%';

/* Select all from a specific device */ 
SELECT *
FROM wap_devices
WHERE parent_ipv4_address = '10.37.124.225';


SELECT *
FROM wap_devices
WHERE parent_ipv4_address = '10.174.173.40';

SELECT COUNT(*) FROM wap_devices;

SELECT DISTINCT mac_address
FROM wap_devices
ORDER BY mac_address;

SELECT *
FROM wap_devices
WHERE mac_address = 'DC:6A:E7:F4:8C:99';

SELECT *
FROM wap_devices
WHERE parent_ipv4_address = '10.39.95.191';

SELECT *
FROM wap_devices_live
WHERE hostname like 'XBOX';

SELECT *
FROM parent_public_ips;
