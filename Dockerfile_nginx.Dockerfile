FROM grafana/grafana 

COPY configurations/university_nginx.conf /etc/nginx/conf.d/university_nginx.conf

