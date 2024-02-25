cd getgrass/
user_id=$1
ip=$2
echo "user_id: $user_id"
echo "ip: $ip"
ps -ef | grep "main.py"| grep -v grep | awk '{print $2}'| xargs kill -9
nohup python3 -u /root/getgrass/main.py $user_id $ip  > my.out 2>&1 &