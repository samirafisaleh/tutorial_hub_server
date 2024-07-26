

if [ -f /.dockerenv ]; then
    
    source .env 
    
    logfile=/logs/tutorial_hub_server/flask/
    echo Log File $logfile
    mkdir -p $logfile

    flask --app main run --host 0.0.0.0

else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "darwin"* ]]; then
    
        source .env 
        logfile=../../../../Logs/tutorial_hub_server/flask/
        echo Log File $logfile
        mkdir -p $logfile

        flask --app main run --host 0.0.0.0

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


