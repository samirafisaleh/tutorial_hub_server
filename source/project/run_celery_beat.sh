

if [ -f /.dockerenv ]; then

    source .env 
    logfile=/Logs/tutorial_hub_server/celery/
    echo Log File $logfile
    mkdir -p $logfile

else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        
        source .env 
        logfile=../../../../Logs/tutorial_hub_server/celery/
        echo Log File $logfile
        mkdir -p $logfile

    elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo $OSTYPE    
    elif [[ "$OSTYPE" == "msys" ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "win32" ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "freebsd"* ]]; then
        echo $OSTYPE
    else
        echo $OSTYPE
    fi
fi



celery --version 
celery -A main beat --loglevel INFO