#echo "----test1----"
#if [ $1 ]
#then
#    num=$(lsof -i:$1 | awk '{print $2}' | sed -n '2p')
#    
#    if [ $num ]
#    then
#        echo "port 30001 is using"
#        echo "pid is $num"
#        echo "projectdir is $(pwdx $num)"
#    else
#        echo "$1 is not running"
#    fi
#else
#    echo "please imput one param"
#fi


echo "----test2----"
read -p "输入用户:" user
username=$(who | awk '{print $1}')

for i in $username
do
    if [ $i = $user ]
    then
        echo "user exist system"
        exit
    fi
done
echo "user not exist system"
