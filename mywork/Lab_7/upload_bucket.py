import boto3
import requests #for downloading internt files
import sys #handling cml

#first, we define a function to get a file from the internet and save it
def download_file(url, filename):
	r = requests.get(url) #get the http link
	with open(filename, 'wb') as f:
		f.write(r.content) #write the content to the file

#next, we define another function to upload the file to s3 and get the presigned URL
def upload_presign(bucket, url, expires_in):
    filename = url.split('/')[-1] #split by / to get the filenane from the url in a desired format - for non-local files
   # filename = url - tried to test local files
    download_file(url, filename)
    s3 = boto3.client('s3', region_name = 'us-east-1') #from directions, create the client 
    s3.upload_file(filename, bucket, filename) #upload file to bucket
    response = s3.generate_presigned_url(
		'get_object',
		Params={'Bucket': bucket, 'Key': filename,
		'ResponseContentType': 'image/jpeg',
		'ResponseContentDisposition': 'inline'}, #i added these additional two args because my images kept automatically downloading, these should force inline display instead
		ExpiresIn=expires_in
		)  #for get_boject, generate the presigned URL, the function generate_presigned_url() comes from the boto3 s3 client, the same goes for the upload_file() function
    print(f"url: {response}") #should output the created url


if __name__ == "__main__":  #checks how the script is going to run
	if len(sys.argv) != 4: #from the sys package, sys.argv contains all of the command line arguments passed into this script, here we clarify that we need 4 args total (script name and 3 inputs) to ensure we have all required info
		print("usage: python3 upload_bucket.py <bucket> <file_url> <expiration_seconds>")
		sys.exit(1) #parameter of 1 here indicates something went wrong with the info provided
	bucket_name = sys.argv[1] #first argument needed (besides script name), should be s3 bucket name
	file_url = sys.argv[2] #second argument needed, should be url of image
	expiration = int(sys.argv[3]) #third argument is the expiration time in seconds, need to make sure this is an integer

	upload_presign(bucket_name, file_url, expiration) #call the previous method to upload the file 
