template_name="citibikes_etl"
cluster_name="citibikes-spark-job"
bucket=gs://enr1qu319-data-engineer-1

gcloud dataproc workflow-templates delete -q $template_name --region=us-central1 &&

gcloud beta dataproc workflow-templates create $template_name --region=us-central1 &&

gcloud beta dataproc workflow-templates set-managed-cluster $template_name \
--region=us-central1 \
--cluster-name=$cluster_name \
--scopes=default \
--master-machine-type n1-standard-2 \
--master-boot-disk-size 20 \
--num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 20 \
--image-version 1.4 &&

gcloud dataproc workflow-templates \
add-job pyspark $bucket/spark-job/City_bike.py \
--region=us-central1 \
--step-id citybikes_etl \
--workflow-template=$template_name &&

gcloud beta dataproc workflow-templates instantiate $template_name --region=us-central1 && 

declare -a Names_of_files=('2013-07_dataselected' \ 
'2013-08_dataselected' \ 
'2013-09_dataselected' \ 
'2013-10_dataselected' \ 
'2013-11_dataselected' \ 
'2013-12_dataselected' \ 
'2014-01_dataselected' \ 
'2014-02_dataselected')  

for folder in ${Names_of_files[@]}; do

   bq load --source_format=CSV \
   data_analysis.city_bikes_data \
   $bucket/citi-bike_data_output/${folder}"_dataselected/*.csv" 

done