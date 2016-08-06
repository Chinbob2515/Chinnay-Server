while :
    do
        java -jar -Xmx712m craftbukkit.jar 2>&1 | tee -a logs/bigLog.txt
        sleep 5
        echo ""
        echo "============================================================"
        echo "                         RESTARTING"
        echo "============================================================"
        echo ""
done
