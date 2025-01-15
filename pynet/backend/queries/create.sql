-- Creating the wap_devices table in the schema
CREATE TABLE wap_devices (
    id SERIAL PRIMARY KEY,
    parent_ipv4_address VARCHAR(15) NOT NULL,  -- Parent private IP (10.x.x.x range)
    child_id INTEGER NOT NULL,                 -- ID of the child device
    child_ipv4_address VARCHAR(15) NOT NULL,   -- Child IP (192.168.x.x range)
    alias VARCHAR(50),                         -- Device alias (optional)
    mac_address VARCHAR(17) NOT NULL,          -- MAC address of the child device
    mac_vendor VARCHAR(255),                   -- Vendor of the MAC address (if available)
    days_present INTERVAL,                     -- Duration (days, hours, minutes)
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP  -- Full timestamp for the event
);

-- Index for quicker lookups on parent IPs
CREATE INDEX idx_parent_ipv4_address ON wap_devices (parent_ipv4_address);

-- Index for quicker lookups on child MAC addresses
CREATE INDEX idx_child_mac_address ON wap_devices (mac_address);

-- Granting privileges to the 'networker' role
GRANT SELECT, INSERT, UPDATE ON wap_devices TO networker;
GRANT USAGE, SELECT ON SEQUENCE wap_devices_id_seq TO networker;
GRANT ALL PRIVILEGES ON wap_devices TO networker;

-- Creating the wap_devices_live table in the schema
CREATE TABLE wap_devices_live (
    id SERIAL PRIMARY KEY,
    parent_ipv4_address VARCHAR(15) NOT NULL,  -- Parent private IP (10.x.x.x range)
    child_ipv4_address VARCHAR(15) NOT NULL,   -- Child IP (192.168.x.x range)
    hostname VARCHAR(50),                       -- Device hostname (optional)
    mac_address VARCHAR(17) NOT NULL,           -- MAC address of the child device
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP  -- Timestamp for the event
);

-- Index for quicker lookups on parent IPs
CREATE INDEX idx_parent_ipv4_address_live ON wap_devices_live (parent_ipv4_address);

-- Index for quicker lookups on child IPs
CREATE INDEX idx_child_ipv4_address_live ON wap_devices_live (child_ipv4_address);

-- Index for quicker lookups on child MAC addresses
CREATE INDEX idx_child_mac_address_live ON wap_devices_live (mac_address);

-- Granting privileges to the 'networker' role
GRANT SELECT, INSERT, UPDATE ON wap_devices_live TO networker;
GRANT USAGE, SELECT ON SEQUENCE wap_devices_live_id_seq TO networker;
GRANT ALL PRIVILEGES ON wap_devices_live TO networker;

ALTER TABLE wap_devices_live RENAME COLUMN hostname TO mac_vendor;

