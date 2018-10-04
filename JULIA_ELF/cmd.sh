bin=$(which julia)
LOG=$(basename $bin).readelf
file $bin > $LOG
readelf -Wa $bin >> $LOG 

echo "-----------" >>$LOG
size $bin >> $LOG
size $(which bash) >>$LOG
echo "-----------" >>$LOG
ls -lh $bin >> $LOG
ls -lh $(which bash) >>$LOG
