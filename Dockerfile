### Creating docker file

# Use the Ubuntu base image
FROM ubuntu

# Install required packages
RUN apt-get update -y
   
RUN apt-get install -y python3 python3-pip

# Create a directory inside the container at /home/doc-bd-a1/
RUN mkdir -p /home/doc-bd-a1/

# make it working dirctory
WORKDIR /home/doc-bd-a1/

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Copy the dataset file to the container
#COPY mxmh_survey_results /home/doc-bd-a1/

# Open the bash shell upon container startup
CMD ["/bin/bash"]