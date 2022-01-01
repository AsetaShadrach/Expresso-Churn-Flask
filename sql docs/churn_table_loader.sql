LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Train.csv'
INTO TABLE user_churn
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS  

(@user_id,@vregion, @vtenure, @vmontant, @vfrequency_rech, @vrevenue , 
@varpu_segment, @vfrequency, @vdata_volume, @von_net, @vorange,
@vtigo, @vzone1, @vzone2, @vmrg, @vregularity, @vtop_pack, 
@vfreq_top_pack,@churn)

SET
user_id = @user_id, 
churn = @churn;