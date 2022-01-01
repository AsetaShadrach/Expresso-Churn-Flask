# Dump the db in a file which we will late upload
# I ran the code on windows powershell
# export the expresso_churn db
mysqldump -u root -p --databases expresso_churn > expressodb.sql

# deleted most values to make the file smaller
# mostly from the users table

