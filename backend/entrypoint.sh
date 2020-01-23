#!/usr/bin/env bash


set -o errexit
set -o pipefail

# set -o nounset


cmd="$@"

function elastic_ready(){
response=$(curl --write-out %{http_code} --silent --output /dev/null elasticsearch:9200/_cluster/health?wait_for_status=yellow&timeout=50s)
if [ $response -ge 200 ]; then
    return 0
else
    return -1
fi
}

function escrapyd_ready(){
response=$(curl --write-out %{http_code} --silent --output /dev/null $SCRAPYD_HOST)
if [ $response -ge 200 ]; then
    return 0
else
    return -1
fi
}

until elastic_ready; do
  >&2 echo "Elastic is unavailable - sleeping"
  sleep 1
done
>&2 echo "Elastic is up - continuing..."

until escrapyd_ready; do
  >&2 echo "Scrapyd is unavailable - sleeping"
  sleep 1
done
>&2 echo "Scrapyd is up - continuing..."



if [ -z "$cmd" ]; then
    if [ "x$localdev" = "xtrue" ]; then
        exec python main.py run -h 0.0.0.0
    else
        exec /app/gunicorn.sh
    fi
else
    exec $cmd
fi