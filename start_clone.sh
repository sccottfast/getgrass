cd getgrass/
user_id=$1
ip=$2
proxy_num=$3
echo "user_id: $user_id"
echo "ip: $ip"
ps -ef | grep "my_clone.py"| grep -v grep | awk '{print $2}'| xargs kill -9
nohup python3 -u /root/getgrass/main_clone.py $user_id $ip $proxy_num > my_clone.out 2>&1 &