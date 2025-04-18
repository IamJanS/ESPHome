# Instructions for Updating the Device Table in README.md

This document provides guidance for creating a Python script to automatically update the device table in the `README.md` file located in the base project directory.

## Steps to Follow

1. **Understand the Structure of `metadata.yaml`**
   - Open `templates/metadata.yaml` to familiarize yourself with its structure.

2. **Review the Current Table in `README.md`**
   - Open `README.md` to locate the table header and verify the expected results.

3. **Check for Existing Script**
   - If `scripts/update_device_table.py` exists, review its content.

4. **Script Placement**
   - The Python script must be placed in the `scripts` directory and named `update_device_table.py`.

## Script Functionality

### Input Files

- Each file in the base project directory with the naming pattern `i[0..9][0..9][0..9]_*.yaml` contains the following keys:
  - `device_name`
  - `device_type`
  - `interface`
  - `board`
  - `platform`

### Key Mapping

The keys map to the following table headers in `README.md`:

| Key           | Table Header |
|---------------|--------------|
| `device_name` | Name         |
| `device_type` | Device       |
| `interface`   | Interface    |
| `board`       | Board        |
| `platform`    | Platform     |

### YAML Parsing

- Strip lines starting with `<<: !include` when loading YAML files to avoid errors with the default Python YAML library.

### Table Update

- Automatically detect the table in `README.md` by locating the header.
- Replace the entire existing table and column header placeholder with updated information.

### Enrich Data with `metadata.yaml`

1. Lookup each key under `metadata` in `templates/metadata.yaml`.
2. If a key is found (e.g., `interface`), retrieve its value (e.g., `name: Sonoff MINI R2`).
3. If a `url` field is present, create a clickable link in the table. For example:
   - `[Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay)`
4. If a key or value is missing, leave the cell empty.
5. If the `url` is missing, exclude the URL.

### Script Execution

- The script will run manually for now.



