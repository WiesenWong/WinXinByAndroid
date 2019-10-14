REM 获取当前页面布局
adb shell uiautomator dump /data/local/tmp/uidump.xml  && adb pull /data/local/tmp/uidump.xml uidump.xml

