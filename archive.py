import os
from dotenv import load_dotenv
from internetarchive import get_session

load_dotenv()

config = {"s3":{"access": os.getenv("S3_ACCESS_KEY"), "secret": os.getenv("S3_SECRET_KEY")}}

session = get_session(config=config)
get_session()

item = session.get_item("TromboneChampCustoms")

for file in os.listdir('.charts/'):
    try:
        print(f"Uploading {file}...")
        item.upload_file('.charts/' + file)
    except Exception as e:
        print(f"Failed to upload {file} to the Internet Archive: {e}")

if not os.listdir('.charts/'):
    print("Nothing to upload!")
