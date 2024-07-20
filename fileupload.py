import os
import boto3
from tqdm import tqdm
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(file_path, bucket_name, s3_path):
    s3 = boto3.client('s3')
    file_size = os.path.getsize(file_path)

    def upload_progress(chunk):
        progress_bar.update(chunk)

    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc=file_path)

    try:
        s3.upload_file(
            file_path,
            bucket_name,
            s3_path,
            Callback=upload_progress
        )
        print(f"\nUpload of {file_path} to s3://{bucket_name}/{s3_path} completed successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"Failed to upload {file_path}: {e}")
    finally:
        progress_bar.close()

def main():
    FILEPATH = "/Users/yinkabakare/downloads"

    FILENAME = input("Enter file name: ")
    FULLPATH = os.path.join(FILEPATH, FILENAME)

    if not os.path.isfile(FULLPATH):
        print("Error: File does not exist in the downloads folder.")
        return

    BUCKET_NAME = "fileupload5678483"
    S3_PATH = FILENAME

    upload_to_s3(FULLPATH, BUCKET_NAME, S3_PATH)

if __name__ == "__main__":
    main()
