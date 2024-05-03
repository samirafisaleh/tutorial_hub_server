# syntax=docker/dockerfile:1

FROM redis

COPY redis.conf /redis.conf

EXPOSE 6379


