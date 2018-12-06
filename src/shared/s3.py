import io, gzip, boto3
from urllib.parse import urlparse

def stream(url):
    s3 = boto3.resource('s3')
    _, bucket_name, key = urlparse(url).path.split('/', 2)
    obj = s3.Object(
        bucket_name=bucket_name,
        key=key
    )
    buffer = io.BytesIO(obj.get()["Body"].read())
    if key.endswith('.gz'):
        return gzip.open(buffer, 'rt')
    else:
        return buffer