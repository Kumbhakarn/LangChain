import os

# Get token from environment
hf_token = os.getenv("HF_TOKEN")

# Check if token exists before assigning
if hf_token:
    os.environ["HF_TOKEN"] = hf_token
else:
    raise EnvironmentError(" Environment variable 'HF_TOKEN' is not set. Please set it before running this script.")
