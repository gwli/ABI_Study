bin=$(which bat)
LOG=$(basename $bin).log
file $bin > $(basename $bin).log
readelf -Wa $bin >> $(basename $bin).log

echo "-----------" >>$LOG
size $bin >> $LOG
size $(which bash) >>$LOG
echo "-----------" >>$LOG
ls -lh $bin >> $LOG
ls -lh $(which bash) >>$LOG
