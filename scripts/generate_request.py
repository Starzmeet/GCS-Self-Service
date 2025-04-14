import os
import shutil

# Get the request name from the environment variable
request_name = os.environ.get('REQUEST_NAME')

if not request_name:
    raise ValueError("REQUEST_NAME environment variable not set.")

# Define the new request folder path
new_request_folder = f'requests/{request_name}'

# Create the new request folder
os.makedirs(new_request_folder, exist_ok=True)

# Define the source template path
template_path = 'template/terraform_template.tf'

# Copy the Terraform template to the new request folder
shutil.copy(template_path, new_request_folder)

# Define the terraform.tfvars path
tfvars_path = os.path.join(new_request_folder, 'terraform.tfvars')

# Replace placeholder values in terraform.tfvars
with open(tfvars_path, 'r+') as tfvars_file:
    content = tfvars_file.read()
    # Replace the placeholder
    content = content.replace('CLUSTER_NAME', request_name)
    # Move the file pointer to the beginning and write the modified content
    tfvars_file.seek(0)
    tfvars_file.write(content)
    tfvars_file.truncate()

print(f'Successfully created request folder: {new_request_folder} and updated terraform.tfvars.')