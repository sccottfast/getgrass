user_id=$1
ip=$2
echo "user_id: $user_id"
echo "ip: $ip"
nohup python3 main.py $user_id ip  > grass.log &