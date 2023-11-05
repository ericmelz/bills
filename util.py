import os
import re
import secrets
import shutil

from pathlib import Path


def move_from_download_to_staging(input_regex, output_regex, download_dir,
                                  staging_dir, 
                                  account_dirs, account,
                                  allow_patterns):
    # Ensure expected staging the directory exists
    account_dir = Path(staging_dir) / account_dirs[account]
    os.makedirs(account_dir, exist_ok=True)
    
    # List the files in the download dir
    for f in os.listdir(download_dir):
        source_path = Path(download_dir) / f
        dest_path = Path(account_dir) / f
        
        # Ensure the file matches an expected downloaded file
        if not re.match(input_regex, f):
            continue
            
        # Compute the new name for the file
        new_filename = re.sub(input_regex, output_regex, f)
        
        # Ensure the new name matches an allowed name
        allowed = all([re.match(p, new_filename) for p in allow_patterns])
        if not allowed:
            continue
            
        # Move the file from download to staging
        shutil.move(source_path, dest_path)
        
        # Rename the file to the new name
        new_dest_path = Path(account_dir) / new_filename
        dest_path.rename(new_dest_path)


def copy_to_destination(account_dirs, staging_dir, destination_dir):
    for account in account_dirs.keys():
        print(f'Copying account {account}')
        account_dir = Path(staging_dir) / account_dirs[account]
        dest_dir = Path(destination_dir) / account_dirs[account]
        os.makedirs(dest_dir, exist_ok=True)
        for f in os.listdir(account_dir):
            source_path = Path(account_dir) / f
            dest_path = Path(dest_dir) / f
            if not os.path.exists(dest_path):
                print(dest_path)
                shutil.copy(source_path, dest_path)    
