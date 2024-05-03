
docker stop data_hub_gunicorn
docker rm data_hub_gunicorn
docker run -d -p 8000:8000 \
            --name data_hub_gunicorn data_hub_server:dev \
            pm_run_gunicorn.sh