# Ansible Cisco Interface Audit Lab

## Objective

Use Ansible to collect interface status information from Cisco devices and generate an operational audit report.

## Prerequisites

- Ansible installed
- Python 3.x
- Cisco IOS XE devices
- SSH connectivity

## Inventory Example

[cisco]
router1 ansible_host=10.1.1.1
router2 ansible_host=10.1.1.2

## Playbook Tasks

1. Connect to devices
2. Gather interface facts
3. Identify interfaces in down state
4. Save output to report
5. Generate audit summary

## Expected Output

- Device Name
- Interface Name
- Interface Status
- IP Address
- Operational State

## Benefits

- Faster audits
- Reduced manual effort
- Consistent reporting
- Improved operational visibility

## Real-World Example

Automated interface health checks across enterprise branch routers to identify failed links before users reported outages.
