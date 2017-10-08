1) When server is booted run the following commands as root.
    yum -y update
    yum install -y aws-cli
    
2) Here you will setup your AWS access, secret, and region.
    aws configure    
    
3) Below command to download and install codedeploy agent
    wget https://aws-codedeploy-ap-southeast-1.s3.amazonaws.com/latest/install
    chmod +x ./install
    sudo ./install auto
    
4) Once it is installed you can verify whether the codedeploy agent is running or not by using the command
    sudo service codedeploy-agent status
    
