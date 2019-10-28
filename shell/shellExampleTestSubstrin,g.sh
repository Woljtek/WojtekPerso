# Test if RET is a substring of XXX

RET=`uname -r`
if [[ "$RET" =~ "el7" ]]; then
    echo "el7 matched"
else
    echo "el7 didn't match"
fi

RET=`virsh net-list`
if [[ "$RET" =~ "vboxnet0" ]]; then
    echo "vboxnet0 matched"
else
    echo "vboxnet0 didn't match"
fi
