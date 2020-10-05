# City-Bike-BigData-Cloud

Citi Bike is New York City’s bike share system, and the largest in the nation. Citi Bike launched in May 2013 and has become an essential part of our transportation network. It's fun, efficient and affordable – not to mention healthy and good for the environment.
Citi Bike, like other bike share systems, consists of a fleet of specially designed, sturdy and durable bikes that are locked into a network of docking stations throughout the city. The bikes can be unlocked from one station and returned to any other station in the system, making them ideal for one-way trips. People use bike share to commute to work or school, run errands, get to appointments or social engagements, and more.
Citi Bike is available for use 24 hours/day, 7 days/week, 365 days/year, and riders have access to thousands of bikes at hundreds of stations across Manhattan, Brooklyn, Queens and Jersey City.

[![](Images/citibike.png)]()          

The task
----

The objective of this project is process citi-bikes data obtained from [Official CitiBike Data Web Page](https://s3.amazonaws.com/tripdata/index.html) in the cloud to storage a daily basis
Tools that were used to accomplish this task:

- Python
- SQL
- Spark
- BigQuery
- Google Workflow
- Apache Airflow
- Linux

[![](Images/google-cloud.jpg)]()  

Data
----
The data includes:

- Trip Duration (seconds)
- Start Time and Date
- Stop Time and Date
- Start Station Name
- End Station Name
- Station ID
- Station Lat/Long
- Bike ID
- User Type (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member)
- Gender (Zero=unknown; 1=male; 2=female)
- Year of Birth

Process
----

The procedure that was taken to process the information is as follows:

- Apply transformation to flight dealys data using Spark-SQL
- Save the transformed data into Big Query partitioned tables
