


if [ -f /.dockerenv ]; then
    
    source .env 
    
    logfile=/logs/tutorial_hub_server/gunicorn/
    echo Log File $logfile
    mkdir -p $logfile

else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "darwin"* ]]; then
    
        source .env 
        logfile=../../../../Logs/tutorial_hub_server/gunicorn/
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

gunicorn --version 

# Print the config
gunicorn -c project/gunicorn.config.py --print-config 'main:app'

# Check the config
echo "Gunicorn: Check Config: Starting..."
gunicorn -c project/gunicorn.config.py --check-config 'main:app'
echo "Gunicorn: Check Config: Complete!"

echo "Gunicorn: Running on $GUNICORN_BIND"
gunicorn -c project/gunicorn.config.py 'main:app'