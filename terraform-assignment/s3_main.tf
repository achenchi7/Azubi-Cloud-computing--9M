provider "aws" {
    access_key = "AKIA6GBMGV2QHSCL6KFO"
    secret_key = "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"
    region = "us-east-1"

    
  
}

resource "aws_s3_bucket" "my_terraform_bucket100" {
    bucket = "myterraformbucket001"
    tags = {
      name = "terrbuck001"
      environment = "prod"
    }
    
}
# COnfigure bucket to allow public read access

resource "aws_s3_bucket_acl" "bucket_aclnew" {
    bucket = aws_s3_bucket.my_terraform_bucket100.id
    acl = "public-read"
  
}

resource "aws_s3_bucket_versioning" "bucket_vers" {
    bucket = aws_s3_bucket.my_terraform_bucket100.id
    versioning_configuration {
      status = "Enabled"
    }
  
}


