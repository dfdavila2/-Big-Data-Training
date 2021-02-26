import sys

# [START storage_upload_file]
from google.cloud import storage

# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\David\PycharmProjects\task1\Project 1\cred\YOUR SA KEY FILE.json"

# set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\David\PycharmProjects\task1\Project 1\cred\YOUR SA KEY FILE.json"

#set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\David\PycharmProjects\task1\Big Data GCP Training-396d0f765521.json"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    bucket_name = "gcp_sample_input"
    source_file_name = "Big-Data-Training-Julio/data/test-dataset.avro"
    destination_blob_name = "https://console.cloud.google.com/storage/browser/gcp_sample_input/input"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

# [END storage_upload_file]

if __name__ == "__main__":
    upload_blob(
        bucket_name=sys.argv[1],
        source_file_name=sys.argv[2],
        destination_blob_name=sys.argv[3],
    )