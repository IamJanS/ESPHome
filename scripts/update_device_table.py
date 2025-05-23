import os
import yaml
import re
import logging

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
README_PATH = os.path.join(BASE_DIR, 'README.md')
METADATA_PATH = os.path.join(BASE_DIR, 'templates', 'metadata.yaml')

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load metadata
def load_metadata():
    with open(METADATA_PATH, 'r') as file:
        return yaml.safe_load(file)

# Parse YAML files in the base directory
def parse_yaml_files():
    data = []
    for filename in os.listdir(BASE_DIR):
        if re.match(r'i\d{3}_.*\.yaml$', filename):
            filepath = os.path.join(BASE_DIR, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                content = re.sub(r'<<: !include.*\n', '', content)  # Strip problematic lines
                content = '\n'.join([line for line in content.splitlines() if '!secret' not in line])  # Skip lines with !secret
                yaml_data = yaml.safe_load(content)
                logging.debug(f"Parsed YAML data from {filename}: {yaml_data}")
                data.append(yaml_data)
    return data

# Enrich data with metadata
def enrich_data(data, metadata):
    enriched = []
    for filename in os.listdir(BASE_DIR):
        if re.match(r'i\d{3}_.*\.yaml$', filename):
            filepath = os.path.join(BASE_DIR, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                content = re.sub(r'<<: !include.*\n', '', content)  # Strip problematic lines
                content = '\n'.join([line for line in content.splitlines() if '!secret' not in line])  # Skip lines with !secret
                yaml_data = yaml.safe_load(content)
                logging.debug(f"Parsed YAML data from {filename}: {yaml_data}")
                enriched_item = {
                    'Name': f"[{filename[:-5]}]({filename})",  # Remove .yaml extension
                    'Device': create_link(yaml_data.get('substitutions', {}).get('device_type', ''), metadata.get('device_type', [])),
                    'Interface': create_link(yaml_data.get('substitutions', {}).get('interface', ''), metadata.get('interface', [])),
                    'Board': create_link(yaml_data.get('substitutions', {}).get('board', ''), metadata.get('board', [])),
                    'Platform': create_link(yaml_data.get('substitutions', {}).get('platform', ''), metadata.get('platform', []))
                }
                enriched.append(enriched_item)
    return enriched

# Create clickable link if URL is present
def create_link(value, metadata_list):
    for meta in metadata_list:
        if meta['name'] == value:
            return f"[{value}]({meta['url']})" if 'url' in meta else value
    return value

# Update the table header to match the actual header in README.md
def update_readme(enriched_data):
    with open(README_PATH, 'r') as file:
        content = file.readlines()

    # Find table header
    start_index = None
    for i, line in enumerate(content):
        if '| Name | Device | Interface | Board | Platform |' in line:  # Corrected header
            start_index = i
            break

    if start_index is None:
        raise ValueError("Table header not found in README.md")

    # Replace table
    end_index = start_index + 1
    while end_index < len(content) and '|' in content[end_index]:
        end_index += 1

    table = generate_table(enriched_data)
    content = content[:start_index] + table + content[end_index:]

    with open(README_PATH, 'w') as file:
        file.writelines(content)

# Generate table from enriched data
def generate_table(data):
    table = ['| Name | Device | Interface | Board | Platform |\n', '|------|--------|-----------|-------|----------|\n']
    for item in sorted(data, key=lambda x: x['Name']):
        row = f"| {item['Name']} | {item['Device']} | {item['Interface']} | {item['Board']} | {item['Platform']} |\n"
        table.append(row)
    return table

if __name__ == '__main__':
    metadata = load_metadata()
    yaml_data = parse_yaml_files()
    enriched_data = enrich_data(yaml_data, metadata['metadata'])
    update_readme(enriched_data)