LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Test.csv'
INTO TABLE expresso_user 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS  

(@user_id,@vregion, @vtenure, @vmontant, @vfrequence_rech, @vrevenue , 
@varpu_segment, @vfrequence, @vdata_volume, @von_net, @vorange,
@vtigo, @vzone1, @vzone2, @vmrg, @vregularity, @vtop_pack, 
@vfreq_top_pack)

SET
user_id = @user_id,
region = NULLIF(@vregion,''),
tenure = NULLIF(@vtenure,''),
montant = NULLIF(@vmontant,''),
frequence_rech = NULLIF(@vfrequence_rech,''),
revenue = NULLIF(@vrevenue,''), 
arpu_segment = NULLIF(@varpu_segment,''),
frequence = NULLIF(@vfrequency ,''),
data_volume = NULLIF(@vdata_volume,''),
on_net = NULLIF(@von_net,''),
orange = NULLIF(@vorange,''),
tigo = NULLIF(@vtigo,''),
zone1 = NULLIF(@vzone1,''),
zone2 = NULLIF(@vzone2,''),
mrg = NULLIF(@vmrg,''), 
regularity = NULLIF(@vregularity,''), 
top_pack = NULLIF(@vtop_pack,''),
freq_top_pack = NULLIF(@freq_top_pack,'')
 
;
