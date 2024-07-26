

if [ -f /.dockerenv ]; then
    
    source .env 

else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo $OSTYPE
    elif [[ "$OSTYPE" == "darwin"* ]]; then
    
        source .env 

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

pip show flower 
echo "Flower: Running on $FLOWER_ADDRESS:$FLOWER_PORT"
celery -A project flower --conf="./project/flower.config.py"