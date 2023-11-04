container_id="your_container_id_here"

# Define the source paths within the container
res_dpre.csv="/home/doc-bd-a1/to/res_dpre.csv"
eda_insight_1.txt="/home/doc-bd-a1/to/eda_insight_1.txt"
eda_insight_2.txt="/home/doc-bd-a1/to/eda_insight_2.txt"
eda_insight_3.txt="/home/doc-bd-a1/to/eda_insight_3.txt"
vis.png="/home/doc-bd-a1/to/vis.png"
k.txt="/home/doc-bd-a1/to/k.txt"

# Define the destination directory on your local machine
local_output_directory="bd-a1/service-result/"

# Copy files from the container to your local machine
docker cp $44a24ff24047f0283e01342b7849ea75e5c477fe52ff23d40004ac88d246b520:$dpre_output $local_output_directory
docker cp $44a24ff24047f0283e01342b7849ea75e5c477fe52ff23d40004ac88d246b520:$eda_output $local_output_directory
docker cp $44a24ff24047f0283e01342b7849ea75e5c477fe52ff23d40004ac88d246b520:$vis_output $local_output_directory
docker cp $44a24ff24047f0283e01342b7849ea75e5c477fe52ff23d40004ac88d246b520:$model_output $local_output_directory

# Close the Docker container
docker stop $44a24ff24047f0283e01342b7849ea75e5c477fe52ff23d40004ac88d246b520