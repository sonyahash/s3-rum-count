import boto3
import os

"""
Global variables
"""
AWS_ACCESS_KEY = "ACCESS KEY HERE"
AWS_SECRET_ACCESS_KEY = "SECRET KEY HERE"
REGION_NAME = "REGION HERE"
BUCKET_NAME = "BUCKET NAME HERE" 

"""
Initializing client
"""
SESSION = boto3.Session(
    aws_access_key_id= AWS_ACCESS_KEY,
    aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
    region_name= REGION_NAME
)

s3 = SESSION.resource('s3')

my_bucket = s3.Bucket(BUCKET_NAME)

cur_path = os.getcwd()
download_path = os.path.join(cur_path, 'state_files')

print("Successfully accessed s3 bucket")

receipt = open("output.txt", "w")

"""
Queries state file from the bucket
"""
tfstate_count = 0
total_rum = 0    
# iterateo over files in my_bucket to find state files
for bucket_obj in my_bucket.objects.all():
    if bucket_obj.key.endswith(".tfstate"):
        if "/" not in bucket_obj.key:
            download = os.path.join(download_path, bucket_obj.key)
            my_bucket.download_file(bucket_obj.key, download)
        # case where maybe it's in a subdirectory or something
        else:
            path, filename = os.path.split(bucket_obj.key)
            download = os.path.join(download_path, filename)
            my_bucket.download_file(bucket_obj.key, download)
        tfstate_count += 1
        print("Retrieved state file: " + bucket_obj.key)
        """
        Runs the script from the bucket
        """
        path = "."
        rum_script = os.path.join(path, "rum_script.sh")          
        state_files_path = os.path.join(path, "state_files")
        os.system("chmod u+x rum_script.sh")                                                                 
        # iterate over all the collected state files
        for state_file in os.listdir(state_files_path):
            f = os.path.join(state_files_path, state_file)
            # runs the rum calc script on all the state files gathered
            if os.path.isfile(f):
                result = os.popen("cat " + "state_files/" + state_file + " | ./rum_script.sh").read()
                receipt.write(state_file + " : " + result)
                total_rum += int(result)
            print("Successfully calced for " + state_file)
            # delete local copy
            os.remove(f)

print("Succesfully retrieved " + str(tfstate_count) + " state files")
receipt.write("Total = " + str(total_rum) + "\n\n")
print("Successfully finished all calculations")
receipt.write("RUM calcs completed")
receipt.close()