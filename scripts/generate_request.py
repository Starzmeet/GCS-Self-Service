import os
import shutil
import sys

# Get the request name from environment variable
request_name = os.environ.get('REQUEST_NAME')
if not request_name:
    print("REQUEST_NAME environment variable not set.")
    sys.exit(1)

# Define the new request folder path
request_folder = f'requests/{request_name.lower()}/'

# Create the new request folder
os.makedirs(request_folder, exist_ok=True)

# Copy the Terraform template into the new folder
shutil.copy('template/terraform_template.tf', f'{request_folder}/terraform.tf')

# Replace placeholder values in terraform.tfvars
with open(f'{request_folder}/terraform.tfvars', 'w') as tfvars:
    tfvars.write(f'CLUSTER_NAME = "{request_name}"
')

print(f'Request folder created at: {request_folder}'}