# Set variables
DATABASE=test1
USERNAME=test1
PASSWORD=test

# Set S3 bucket name and region
S3_BUCKET_NAME=your-s3-bucket-name
AWS_REGION=your-aws-region

# Set backup file name and path date will be current date and time when you are creating this job
BACKUP_FILENAME=backup-$(date +%Y-%m-%d-%H-%M-%S).sql
BACKUP_PATH=/tmp/$BACKUP_FILENAME

# Create backup using pg_dump
pg_dump -U $USERNAME -h localhost $DATABASE > $BACKUP_PATH

# Copy backup file to S3 bucket
aws s3 cp $BACKUP_PATH s3://$S3_BUCKET_NAME/$BACKUP_FILENAME --region $AWS_REGION

# Remove backup file from local directory
rm $BACKUP_PATH