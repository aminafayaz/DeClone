import os
import hashlib


def read_file_in_chunks(file_path,chunk_size = 4096):
    try:
        with open(file_path,'rb')as f:
            while chunk:= f.read(chunk_size):
                yield chunk
    except Exception as e:
        print(f"Error reading {file_path}: {e}")


def hash_file(file_path):
    hasher = hashlib.sha256()
    for chunk in read_file_in_chunks(file_path):
        hasher.update(chunk)
    return hasher.hexdigest()


def scan_for_duplicates(folder_path):
    duplicates = {}
    if os.path.exists(folder_path):
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                full_path = os.path.join(dirpath,filename)

                try:
                    file_hash = hash_file(full_path)
                    if file_hash:
                        file_size = os.path.getsize(full_path)
                        file_info = {"path": full_path,"size":file_size}
                        if file_hash in duplicates:
                            duplicates[file_hash].append(file_info)
                        else:
                            duplicates[file_hash] = [file_info]
                except Exception as e:
                    print(f"Skipping {full_path}: {e}")
           
        
        result = {}
        for hash_, files in duplicates.items():
            if len(files) > 1:
                result[hash_] = files

        return result   
    
    else:
        print("Invalid folder path.")
        return {}