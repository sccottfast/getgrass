cd getgrass/
user_id=$1
ip=$2
proxy_num=$3
echo "user_id: $user_id"
echo "ip: $ip"
ps -ef | grep "main_clone_4.py"| grep -v grep | awk '{print $2}'| xargs kill -9
nohup python3 -u /root/getgrass/main_clone_4.py $user_id $ip $proxy_num > main_clone_4.out 2>&1 &